from django.urls import path, re_path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    re_path(route=r'^register/?$', view=views.register, name='register'),
    re_path(route=r'^login/?$', view=views.login, name='login'),
]
