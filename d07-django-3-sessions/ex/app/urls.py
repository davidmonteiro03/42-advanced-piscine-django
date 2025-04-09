from django.urls import path, re_path
from . import views

urlpatterns = [
    path(route="",
         view=views.index),
    re_path(route=r"^register/?$",
         view=views.register),
    re_path(route=r"^login/?$",
         view=views.login),
    re_path(route=r"^logout/?$",
         view=views.logout),
]
