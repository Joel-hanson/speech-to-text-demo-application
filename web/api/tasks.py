from celery import shared_task
from celery.utils.log import get_task_logger
from django_celery_results.models import states

from .models import TaskRun
from .utils import send_status_update

celery_log = get_task_logger(__name__)


@shared_task(bind=True, name="backend.save_speech_results")
def save_speech_results(
    self,
    id,
    text,
    duration,
):
    celery_log.debug("Entered save_speech_results %s task_id: %s", id, self.request.id)

    try:
        task_run = TaskRun.objects.get(id=id)
        task_run.status = states.SUCCESS
        task_run.text = text
        task_run.save()
        send_status_update(task_run)
    except Exception as e:
        celery_log.exception(e)

    return {"id": id, "text": text, "duration": duration}
