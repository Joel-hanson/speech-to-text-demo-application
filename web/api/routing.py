from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/s2t/(?P<lobby_name>\w+)/$", consumers.SpeechToTextConsumer.as_asgi()),
]
