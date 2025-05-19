from django.urls import re_path
from account.views import HomeView, LoginView, LogoutView

urlpatterns = [
    re_path(r'^/?$', HomeView.as_view(), name='home'),
    re_path(r'^/login/?$', LoginView.as_view(), name='login'),
    re_path(r'^/logout/?$', LogoutView.as_view(), name='logout'),
]
