from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from chat.models import Room, Message
from chat.forms import ChatMessageForm


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = ChatMessageForm()
        context_data['history'] = list(Message.objects.filter(room=context_data['chat_room']).order_by('-timestamp')[:3])
        context_data['history'].reverse()
        return context_data
