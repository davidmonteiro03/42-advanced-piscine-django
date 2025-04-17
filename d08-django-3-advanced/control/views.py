from django.shortcuts import render
from django.views.generic import ListView
from control.models import Article


class ArticlesView(ListView):
    model = Article
