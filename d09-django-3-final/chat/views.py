from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from chat.models import Room


class Home(ListView):
    model = Room
    template_name = 'chat/home.html'
    context_object_name = 'chat_rooms'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("account:home"))
        return super().get(request, *args, **kwargs)


class ChatRoom(DetailView):
    model = Room
    template_name = 'chat/room.html'
    context_object_name = 'chat_room'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("account:home"))
        return super().get(request, *args, **kwargs)
