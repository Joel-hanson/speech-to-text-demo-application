import asyncio

from celery import shared_task
from celery.utils.log import get_task_logger
from channels.layers import get_channel_layer

from .consumers import LOBBY_GROUP_NAME
from .models import TaskRun
from .serializers import TaskRunsDetailedSerializer
from .utils import send_status_update

celery_log = get_task_logger(__name__)


@shared_task(name="backend.save_speech_results")
def save_speech_results(
    id,
    text,
):
    """
    Save speech results to db
    :param id: id of the file
    :param file: file path
    :param text: text
    :param created_at: created at
    :param updated_at: updated at
    :return: None
    """
    celery_log.info("Entered save_speech_results %s", id)
    celery_log.info("Text: %s", text)

    task_run = TaskRun.objects.get(id=id)
    task_run.status = "COMPLETED"
    task_run.text = text
    task_run.save()
    task_run_data = TaskRunsDetailedSerializer(task_run).data
    send_status_update(task_run_data)

    return task_run_data
