from django.urls import re_path, path
from control.views import Articles, Home, Login


urlpatterns = [
    re_path(r'^articles/?$', Articles.as_view(), name='articles'),
    path('', Home.as_view(), name='home'),
    re_path(r'^login/?$', Login.as_view(), name='login'),
]
