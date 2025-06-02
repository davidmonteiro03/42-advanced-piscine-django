from django.urls import re_path
from chat.views import Home, ChatRoom

app_name = 'chat'

urlpatterns = [
    re_path(r'^/?$', Home.as_view(), name='home'),
    re_path(r'^rooms/(?P<name>[^/]+)/?$', ChatRoom.as_view(), name='room'),
]
