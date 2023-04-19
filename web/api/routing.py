from django.urls import re_path

from .consumers import S2TConsumer

websocket_urlpatterns = [
    re_path(r"ws/s2t/(?P<lobby_name>\w+)/$", S2TConsumer.as_asgi()),
]
