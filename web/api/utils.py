import asyncio

from channels.layers import get_channel_layer

from .consumers import LOBBY_GROUP_NAME
from .models import TaskRun


def send_status_update(data):
    print(data)
    channel_layer = get_channel_layer()
    message = {
        "type": "status_update",
        "data": {
            "id": data.get("id"),
            "status": data.get("status"),
            "text": data.get("text"),
            "service": data.get("service"),
            "date": data.get("date"),
            "time": data.get("time"),
            "title": data.get("title"),
            "upload": {
                "id": data.get("upload", {}).get("id"),
                "file": data.get("upload", {}).get("file"),
                "created_at": data.get("upload", {}).get("created_at"),
                "updated_at": data.get("upload", {}).get("updated_at"),
            },
        },
    }
    asyncio.run(
        channel_layer.group_send(  # type: ignore
            LOBBY_GROUP_NAME, {"type": "send_message", "message": message}
        )
    )


def create_task_run(id):
    task_run = TaskRun.objects.create(
        upload_id=id,
        text="",
        service="speech-service",
    )

    return task_run
