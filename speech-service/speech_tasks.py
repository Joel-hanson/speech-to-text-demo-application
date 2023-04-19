import tempfile
from time import time
from urllib import request

from celery import shared_task
from celery.utils.log import get_task_logger
from celery_config import celery
from speech_utils import recognize_speech

celery_log = get_task_logger(__name__)


# task name: run_speech_recognition
@shared_task(bind=True, name="speech-service.SpeechRecognition")
def run_speech_recognition(
    self,
    id,
    file,
    created_at,
    updated_at,
):
    """
    Run speech recognition on a file

    :param id: id of the file
    :param file: file url where the file is stored
    :param created_at: created_at of the file
    :param updated_at: updated_at of the file
    :return: json response to be stored in the database
    """
    celery_log.info(
        "Entered run_speech_recognition %s task_id: %s", id, self.request.id
    )

    time_start = time()
    # Get the file from the url
    file_url = file.replace("localhost", "web")

    # Run speech recognition on the file
    speech_text = ""
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        temp_file_name = temp_file.name
        request.urlretrieve(file_url, temp_file_name)
        speech_text = recognize_speech(temp_file_name)
        temp_file.close()

    time_end = time()

    # send a redis message to trigger the celery task
    response = {
        "id": id,
        "duration": time_end - time_start,
        "text": speech_text,
    }
    response_task_signature = celery.signature("backend.save_speech_results").set(
        task_id=self.request.id
    )
    response_task_signature.apply_async(
        args=[
            response["id"],
            response["text"],
            response["duration"],
        ],
    )

    return response
