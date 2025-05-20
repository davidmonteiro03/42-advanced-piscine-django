from django.views.generic import ListView, DetailView
from chat.models import Room as ChatRoom
from typing import Any


class Home(ListView):
    model = ChatRoom
    template_name = 'chat/home.html'
    context_object_name = 'chat_rooms'


class ChatRoom(DetailView):
    model = ChatRoom
    template_name = 'chat/room.html'
    context_object_name = 'chat_room'
    slug_field = 'name'
    slug_url_kwarg = 'name'
