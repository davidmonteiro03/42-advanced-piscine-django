from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json


class ChatConsumer(AsyncWebsocketConsumer):
    userlist = {}

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        self.username = self.scope['user'].username
        self.socketfd = self.scope['client'][1]

        if not self.userlist.get(self.room_name):
            self.userlist[self.room_name] = {}

        self.userlist[self.room_name][f"{self.socketfd}"] = self.username

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.join()

    async def disconnect(self, code):
        del self.userlist[self.room_name][f"{self.socketfd}"]

        await self.leave()

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        from django.contrib.auth.models import User
        from chat.models import Room, Message

        json_data = json.loads(text_data)

        text: str = str(json_data['text']).strip()

        if len(text) > 0:
            user: User = await database_sync_to_async(User.objects.get)(username=self.username)
            room: Room = await database_sync_to_async(Room.objects.get)(name=self.room_name)

            await database_sync_to_async(Message.objects.create)(user=user, room=room, text=text)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': "chat_message",
                    'cmd': "message",
                    'data': {
                        'text': text,
                        'username': self.username
                    }
                }
            )

    async def join(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'cmd': "join",
                'data': {
                    'username': self.username,
                }
            }
        )

        await self.list()

    async def leave(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'cmd': "leave",
                'data': {
                    'username': self.username
                }
            }
        )

        await self.list()

    async def list(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'cmd': "list",
                'data': {
                    'userlist': self.userlist[self.room_name]
                }
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'cmd': event['cmd'],
            'data': event['data']
        }))
