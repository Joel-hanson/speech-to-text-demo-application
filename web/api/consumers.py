import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

LOBBY_GROUP_NAME = "sock_lobby"


class S2TConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.lobby_name = self.scope["url_route"]["kwargs"]["lobby_name"]
        self.group_name = "sock_%s" % self.lobby_name
        print("Connected to group ", self.group_name)
        # Join room group
        await self.channel_layer.group_add(self.group_name, self.channel_name)  # type: ignore

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)  # type: ignore

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(  # type: ignore
            self.group_name, {"type": "send_message", "message": message}
        )

    # Receive message from room group
    async def send_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
