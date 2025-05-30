from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_join",
                'data': {
                    'username': self.scope['user'].username
                }
            }
        )

    async def chat_join(self, event):
        data = event['data']
        username = data['username']
        message = f"{username} has joined the chat"

        await self.send(text_data=json.dumps({
            'message': message
        }))
