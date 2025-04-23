from django.views.generic import ListView, RedirectView, FormView, DetailView
from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from typing import Any
from control.models import Article, UserFavouriteArticle
from control.utils import get_time_diff_description


class Articles(ListView):
    model = Article
    template_name = 'control/articles.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        datetime_now = timezone.now()
        articles: models.BaseManager[Article] = context['articles']
        for article in articles:
            article.when = get_time_diff_description(datetime_now, article.created)
        return context


class Home(RedirectView):
    url = reverse_lazy('articles')


class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'control/login.html'
    success_url = reverse_lazy('home')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: Any) -> HttpResponse:
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if not user:
            return
        login(self.request, user)
        return super().form_valid(form)


class Publications(ListView):
    model = Article
    template_name = 'control/publications.html'
    context_object_name = 'publications'


class Detail(DetailView):
    model = Article
    template_name = 'control/detail.html'
    context_object_name = 'article'


class Logout(RedirectView):
    url = reverse_lazy('home')

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated is True:
            logout(request)
        return super().get(request, *args, **kwargs)


class Favourites(ListView):
    model = UserFavouriteArticle
    template_name = 'control/favourites.html'
    context_object_name = 'favourites'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
