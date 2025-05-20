from django.urls import re_path
from chat.views import Home, ChatRoom

urlpatterns = [
    re_path(r'^/?$', Home.as_view(), name='home'),
    re_path(r'^rooms/(?P<name>[^/]+)/?$', ChatRoom.as_view(), name='chat_room'),
]
