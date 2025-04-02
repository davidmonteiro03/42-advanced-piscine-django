from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import ex.settings as settings
import random
from . import forms

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if not request.session.get(key='user_name'):
        request.session['user_name'] = random.choice(seq=settings.USERS)
        request.session.set_expiry(value=settings.SESSION_COOKIE_AGE)
    return render(request=request,
                  template_name='app/index.html',
                  context={'user_name': request.session['user_name'],
                           'time_to_wait': settings.SESSION_COOKIE_AGE})

def register(request: HttpRequest) -> HttpResponse:
    return render(request=request,
                  template_name='app/register.html',
                  context={'form': forms.RegistrationForm()})

def login(request: HttpRequest) -> HttpResponse:
    return render(request=request,
                  template_name='app/login.html')
