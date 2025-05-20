from django.views.generic import FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from typing import Any
import json


class Home(FormView):
    form_class = AuthenticationForm
    template_name = 'account/home.html'


class Login(FormView):
    form_class = AuthenticationForm

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return HttpResponseNotAllowed(['POST'])

    def form_valid(self, form: AuthenticationForm) -> HttpResponse | JsonResponse:
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return JsonResponse({'html': render_to_string('account/login.html', request=self.request)}, status=200)

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse | JsonResponse:
        return HttpResponse(json.dumps({'error': "Invalid username or password."}), status=401)


class Logout(View):
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        logout(request)
        return JsonResponse({'html': render_to_string('account/login.html', {'form': AuthenticationForm()}, request)}, status=200)

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return HttpResponseNotAllowed(['POST'])
