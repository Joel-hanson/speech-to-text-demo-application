import asyncio

from channels.layers import get_channel_layer

from .consumers import LOBBY_GROUP_NAME
from .models import TaskRun
from .serializers import TaskRunsDetailedSerializer

# #: Task state is unknown (assumed pending since you know the id).
# PENDING = 'PENDING'
# #: Task was received by a worker (only used in events).
# RECEIVED = 'RECEIVED'
# #: Task was started by a worker (:setting:`task_track_started`).
# STARTED = 'STARTED'
# #: Task succeeded
# SUCCESS = 'SUCCESS'
# #: Task failed
# FAILURE = 'FAILURE'
# #: Task was revoked.
# REVOKED = 'REVOKED'
# #: Task was rejected (only used in events).
# REJECTED = 'REJECTED'
# #: Task is waiting for retry.
# RETRY = 'RETRY'
# IGNORED = 'IGNORED'


def send_status_update(task_run):
    data = TaskRunsDetailedSerializer(task_run).data
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
