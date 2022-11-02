import json
from channels.generic.websocket import WebsocketConsumer, AsyncConsumer
import asyncio

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.username = "Anonymous"
        self.accept()
        self.send(text_data="[Welcome %s!]" % self.username)

    def receive(self, *, text_data):
        if text_data.startswith("/name"):
            self.username = text_data[5:].strip()
            self.send(text_data="[set your username to %s]" % self.username)
        else:
            self.send(text_data=self.username + ": " + text_data)

    def disconnect(self, message):
        pass


# class LogConsumer(WebsocketConsumer):
#
#     def connect(self, message):
#         Log.objects.create(
#             type="connected",
#             client=self.scope["client"],
#         )

class PingConsumer(AsyncConsumer):
    async def websocket_connect(self, message):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, message):
        await asyncio.sleep(1)
        await self.send({
            "type": "websocket.send",
            "text": "pong",
        })

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#
#     def disconnect(self, close_code):
#         pass
#
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#
#         self.send(text_data=json.dumps({"message": message}))

# class ChatConsumer(WebsocketConsumer):

# def connect(self):
#     self.username = "Anonymous"
#     self.accept()
#     self.send(text_data="[Welcome %s!]" % self.username)
#
# # def receive(self, *, text_data):
# def receive(self, text_data, **kwargs):
#     text_data_json = json.loads(text_data)
#     message = text_data_json["message"]
#
#     self.send(text_data=json.dumps({"message": message}))
#
# # if text_data.startswith("/name"):
#     #     self.username = text_data[5:].strip()
#     #     self.send(text_data="[set your username to %s]" % self.username)
#     # else:
#     #     self.send(text_data=self.username + ": " + text_data)
#
# def disconnect(self, message):
#     pass


