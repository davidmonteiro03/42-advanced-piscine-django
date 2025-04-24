from django.views.generic import ListView, RedirectView, FormView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.forms import BaseModelForm
from django.utils import translation
from articles import settings
from control.models import Article, UserFavouriteArticle
from control.forms import LoginForm, ArticleForm, UserFavouriteArticleForm
from typing import Any


class Articles(ListView):
    model = Article
    template_name = 'control/articles.html'
    context_object_name = 'articles'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            lang = self.kwargs['lang']
            if lang not in dict(settings.LANGUAGES):
                return redirect(reverse_lazy('articles'))
        except Exception:
            lang = settings.LANGUAGE_CODE
        translation.activate(lang)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        try:
            context_data['lang'] = self.kwargs['lang']
        except Exception:
            context_data['lang'] = settings.LANGUAGE_CODE
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created')


class Home(RedirectView):
    url = reverse_lazy('articles')


class Login(FormView):
    form_class = LoginForm
    template_name = 'control/login.html'
    success_url = reverse_lazy('home')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return redirect(reverse_lazy('home'))

    def form_valid(self, form: Any) -> HttpResponse:
        credentials = {'username': form.cleaned_data['username'],
                       'password': form.cleaned_data['password']}
        user = authenticate(self.request, **credentials)
        if not user:
            return
        login(self.request, user)
        return super().form_valid(form)


class Publications(ListView):
    model = Article
    template_name = 'control/publications.html'
    context_object_name = 'publications'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class Detail(DetailView):
    model = Article
    template_name = 'control/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        try:
            article: Article = context_data['article']
            context_data['in_favourites'] = UserFavouriteArticle.objects.filter(user=self.request.user, article=article).exists()
        except Exception:
            pass
        return context_data


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


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'control/register.html'
    success_url = reverse_lazy('home')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        credentials = {'username': form.cleaned_data['username'],
                       'password': form.cleaned_data['password1']}
        user = authenticate(self.request, **credentials)
        if not user:
            return response
        login(self.request, user)
        return response


class Publish(CreateView):
    form_class = ArticleForm
    template_name = 'control/publish.html'
    success_url = reverse_lazy('publications')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('home'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddToFavourite(CreateView):
    model = UserFavouriteArticle
    form_class = UserFavouriteArticleForm
    success_url = reverse_lazy('favourites')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return redirect(reverse_lazy('home'))

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        try:
            article = get_object_or_404(Article, id=self.kwargs['pk'])
            if not article:
                return
            form.instance.user = self.request.user
            form.instance.article = article
            return super().form_valid(form)
        except Exception:
        	return redirect(reverse_lazy('home'))
