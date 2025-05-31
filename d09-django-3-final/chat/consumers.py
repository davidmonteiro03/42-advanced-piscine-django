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
                'type': "chat_message",
                'cmd': "join",
                'data': {
                    'username': self.scope['user'].username
                }
            }
        )

    async def receive(self, text_data=None, bytes_data=None):
        json_data = json.loads(text_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat_message",
                'cmd': "message",
                'data': {
                    'text': json_data['text'],
                    'username': self.scope['user'].username
                }
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'cmd': event['cmd'],
            'data': event['data']
        }))
