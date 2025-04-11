from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . import forms
from .models import CustomUser, Tip
import life_pro_tips.settings as settings
import datetime
import random
import copy


def generate_random_user_name(request: HttpRequest) -> tuple[str, int]:
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
    session_expiry = settings.SESSION_EXPIRY + 1
    if not request.session.get(key='user_name') or not request.session.get(key='timestamp'):
        request.session['user_name'] = random.choice(settings.USERNAMES)
        request.session['timestamp'] = datetime.datetime.strftime(datetime.datetime.now(),
                                                                  DATE_FORMAT)
    else:
        old_time = datetime.datetime.strptime(request.session['timestamp'],
                                              DATE_FORMAT)
        current_time = datetime.datetime.now()
        diff_time = current_time - old_time
        if diff_time.seconds >= settings.SESSION_EXPIRY:
            request.session['user_name'] = random.choice(seq=[u for u in settings.USERNAMES
                                                              if u != request.session['user_name']])
            request.session['timestamp'] = datetime.datetime.strftime(datetime.datetime.now(),
                                                                      DATE_FORMAT)
        else:
            session_expiry = settings.SESSION_EXPIRY - diff_time.seconds + 1
    return request.session['user_name'], session_expiry


def index(request: HttpRequest) -> HttpResponse:
    DATE_FORMAT = "%d %B %Y"
    context = {}
    if request.user.is_authenticated:
        if request.session.get(key='user_name'):
            del request.session['user_name']
        if request.session.get(key='timestamp'):
            del request.session['timestamp']
        custom_user = CustomUser.objects.filter(username=request.user.username).first()
        context['form'] = forms.TipForm()
        context['tips'] = []
        tips = copy.deepcopy(Tip.objects.all())
        for t in tips:
            t_dict = {}
            t_dict['id'] = t.id
            t_dict['content'] = t.content
            t_dict['author'] = t.author
            t_dict['date'] = t.date.strftime(DATE_FORMAT)
            t_dict['num_up_votes'] = len(t.upvotes.all())
            t_dict['num_down_votes'] = len(t.downvotes.all())
            t_dict['can_delete_tip'] = t.author == custom_user or custom_user.is_staff
            t_dict['can_upvote_tip'] = not any([uv == custom_user for uv in t.upvotes.all()])
            t_dict['can_downvote_tip'] = not any([dv == custom_user for dv in t.downvotes.all()]) and \
                (t.author == custom_user or custom_user.can_downvote_tips)
            context['tips'].append(t_dict)
    else:
        context['user_name'], context['session_expiry'] = generate_random_user_name(request=request)
    return render(request=request,
                  template_name="control/index.html",
                  context=context)


def register(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        return redirect(to="/")
    if request.POST:
        form = forms.RegistrationForm(data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            password_confirmation = form.cleaned_data.get('password_confirmation')
            if CustomUser.objects.filter(username=user_name).exists():
                form.add_error(field='user_name',
                               error="User already exists.")
            elif password != password_confirmation:
                form.add_error(field='password',
                               error="Passwords don't match.")
            else:
                user = CustomUser.objects.create_user(username=user_name,
                                                      password=password)
                auth_login(request=request,
                           user=user)
                return redirect(to="/")
        context['form'] = form
        context['user_name'], context['session_expiry'] = generate_random_user_name(request=request)
    else:
        context['form'] = forms.RegistrationForm()
        context['user_name'], context['session_expiry'] = generate_random_user_name(request=request)
    return render(request=request,
                  template_name="control/register.html",
                  context=context)


def login(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        return redirect(to="/")
    if request.POST:
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request,
                                username=user_name,
                                password=password)
            if not CustomUser.objects.filter(username=user_name).exists():
                form.add_error(field="user_name",
                               error="User doesn't exist.")
            elif not user:
                form.add_error(field="password",
                               error="Wrong password.")
            else:
                auth_login(request=request,
                           user=user)
                return redirect(to="/")
        context['form'] = form
        context['user_name'], context['session_expiry'] = generate_random_user_name(request=request)
    else:
        context['form'] = forms.LoginForm()
        context['user_name'], context['session_expiry'] = generate_random_user_name(request=request)
    return render(request=request,
                  template_name="control/login.html",
                  context=context)


def logout(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        auth_logout(request=request)
    return redirect(to="/")


def create_tip(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        if request.POST:
            form = forms.TipForm(data=request.POST)
            if form.is_valid():
                Tip.objects.create(content=form.cleaned_data.get('content'),
                                   author=request.user)
                return redirect(to="/")
            context['form'] = form
        return render(request=request,
                      template_name="control/index.html",
                      context=context)
    return redirect(to="/")


def delete_tip(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        custom_user = CustomUser.objects.filter(username=request.user.username).first()
        if request.POST and custom_user:
            tip_id = request.POST.get(key="tip_id")
            tip = Tip.objects.filter(id=tip_id).first()
            if tip and (custom_user.is_staff or tip.author == custom_user):
                tip.delete()
            return redirect(to="/")
        return render(request=request,
                      template_name="control/index.html",
                      context=context)
    return redirect(to="/")


def upvote_tip(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        custom_user = CustomUser.objects.filter(username=request.user.username).first()
        if request.POST and custom_user:
            tip_id = request.POST.get(key="tip_id")
            tip = Tip.objects.filter(id=tip_id).first()
            if tip:
                tip.downvotes.remove(custom_user)
                tip.upvotes.add(custom_user)
            return redirect(to="/")
        return render(request=request,
                      template_name="control/index.html",
                      context=context)
    return redirect(to="/")


def downvote_tip(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        custom_user = CustomUser.objects.filter(username=request.user.username).first()
        if request.POST and custom_user:
            tip_id = request.POST.get(key="tip_id")
            tip = Tip.objects.filter(id=tip_id).first()
            if tip and (custom_user.can_downvote_tips or tip.author == custom_user):
                tip.upvotes.remove(custom_user)
                tip.downvotes.add(custom_user)
            return redirect(to="/")
        return render(request=request,
                      template_name="control/index.html",
                      context=context)
    return redirect(to="/")
