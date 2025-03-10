from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^/init/?$', views.init),
    re_path(r'^/populate/?$', views.populate),
    re_path(r'^/display/?$', views.display),
    re_path(r'^/update/?$', views.update),
]
