from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . import forms
import ex.settings as set
import datetime
import random

# Create your views here.
def generate_random_user_name(request: HttpRequest) -> str:
    _format = "%Y-%m-%d %H:%M:%S.%f"
    if not request.session.get(key='user_name'):
        request.session['user_name'] = random.choice(set.USERNAMES)
    if not request.session.get(key='timestamp'):
        request.session['timestamp'] = datetime.datetime.strftime(datetime.datetime.now(),
                                                                  _format)
    _old_time = datetime.datetime.strptime(request.session['timestamp'],
                                           _format)
    _now_time = datetime.datetime.now()
    if (_now_time - _old_time).seconds > set.SESSION_EXPIRY:
        request.session['user_name'] = random.choice(seq=[u for u in set.USERNAMES
                                                          if u != request.session['user_name']])
        request.session['timestamp'] = datetime.datetime.strftime(datetime.datetime.now(),
                                                                  _format)
    return request.session['user_name']

def index(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.user.is_authenticated:
        if request.session.get(key='user_name'):
            del request.session['user_name']
        if request.session.get(key='timestamp'):
            del request.session['timestamp']
    else:
        context['user_name'] = generate_random_user_name(request=request)
        context['session_expiry'] = set.SESSION_EXPIRY
    return render(request=request,
                  template_name="app/index.html",
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
            if User.objects.filter(username=user_name).exists():
                form.add_error(field='user_name',
                               error="User already exists.")
            elif password != password_confirmation:
                form.add_error(field='password',
                               error="Passwords don't match.")
            else:
                user =  User.objects.create_user(username=user_name,
                                                 password=password)
                auth_login(request=request,
                           user=user)
                return redirect(to="/")
        context['form'] = form
        context['user_name'] = generate_random_user_name(request=request)
    else:
        context['form'] = forms.RegistrationForm()
        context['user_name'] = generate_random_user_name(request=request)
    return render(request=request,
                  template_name="app/register.html",
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
            if not User.objects.filter(username=user_name).exists():
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
        context['user_name'] = generate_random_user_name(request=request)
    else:
        context['form'] = forms.LoginForm()
        context['user_name'] = generate_random_user_name(request=request)
    return render(request=request,
                  template_name="app/login.html",
                  context=context)


def logout(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        auth_logout(request=request)
    return redirect(to="/")
