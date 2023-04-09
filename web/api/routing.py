from django.urls import path, re_path

from .consumers import SpeechToTextConsumer
from .views import UploadAPIView

websocket_urlpatterns = [
    re_path(r"ws/s2t/(?P<lobby_name>\w+)/$", SpeechToTextConsumer.as_asgi()),
]
