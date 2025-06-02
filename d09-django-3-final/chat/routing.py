from django.urls import re_path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^chatrooms/(?P<room_name>[^/]+)/?$', ChatConsumer.as_asgi()),
]
