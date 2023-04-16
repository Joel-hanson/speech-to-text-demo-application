import os
from time import sleep, time

from celery import shared_task
from celery.utils.log import get_task_logger
from celery_config import celery

celery_log = get_task_logger(__name__)


# task name: run_speech_recognition
@shared_task(name="speech-service.SpeechRecognition")
def run_speech_recognition(
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
    celery_log.info("Entered run_speech_recognition %s", id)

    time_start = time()
    # Get the file from the url
    file = file.replace("localhost", "web")
    # response = urllib.request.urlopen(file)
    # data = response.read()
    # text = data.decode("utf-8")
    # print(text)

    # Run speech recognition on the file
    # TODO
    sleep(10)

    # Save the result
    # TODO

    time_end = time()
    celery_log.info("Exited run_speech_recognition %s", id)

    # send a redis message to trigger the celery task
    # recognize_speech(file)
    response = {
        "id": id,
        "completed_in": time_end - time_start,
        "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    }
    celery.autodiscover_tasks()
    celery.signature(
        "backend.save_speech_results",
        args=[
            response["id"],
            response["text"],
        ],
    ).apply_async()

    return response
