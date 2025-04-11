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
    re_path(route=r"^create-tip/?$",
         view=views.create_tip),
    re_path(route=r"^delete-tip/?$",
         view=views.delete_tip),
    re_path(route=r"^upvote-tip/?$",
         view=views.upvote_tip),
    re_path(route=r"^downvote-tip/?$",
         view=views.downvote_tip),
]
