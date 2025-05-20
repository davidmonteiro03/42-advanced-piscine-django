from django.urls import re_path
from account.views import Home, Login, Logout

urlpatterns = [
    re_path(r'^/?$', Home.as_view(), name='home'),
    re_path(r'^/login/?$', Login.as_view(), name='login'),
    re_path(r'^/logout/?$', Logout.as_view(), name='logout'),
]
