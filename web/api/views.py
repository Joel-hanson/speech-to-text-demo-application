from backend.celery import app
from django.conf import settings
from django_celery_results.models import states
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

import redis

from .models import TaskRun, Upload
from .serializers import (
    TaskRunsDetailedSerializer,
    TaskRunsSerializer,
    UploadDetailedSerializer,
    UploadSerializer,
)
from .utils import create_task_run, send_status_update


# Create your views here.
class UploadAPIView(ModelViewSet):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all().order_by("-id")
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        # create a new upload
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # create a task run
        task_run = create_task_run(serializer.data["id"])
        task_run.status = states.PENDING
        task_run.save()
        send_status_update(task_run)
        try:
            self.run_speech_task(
                serializer, task_run, task_name="speech-service.SpeechRecognition"
            )
        except Exception:
            task_run.status = states.FAILURE
            task_run.save()
            # send_status_update(task_run)
            return Response(
                serializer.data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                headers=headers,
            )

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def run_speech_task(self, serializer, task_run, task_name):
        app.autodiscover_tasks()
        task_signature = app.signature(
            task_name,
        )
        task_id = task_signature.apply_async(
            args=[
                task_run.id,  # type: ignore
                serializer.data["file"],
                serializer.data["created_at"],
                serializer.data["updated_at"],
            ]
        )
        task_run.status = states.STARTED
        task_run.task_id = task_id
        task_run.save()
        send_status_update(task_run)

    @action(detail=False, methods=["get"], url_path="detailed")
    def detailed(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).order_by("-id")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UploadDetailedSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="task_runs")
    def task_runs(self, request, *args, **kwargs):
        queryset = TaskRun.objects.all().order_by("-id")
        serializer = TaskRunsDetailedSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskRunsAPIView(ModelViewSet):
    serializer_class = TaskRunsSerializer
    queryset = TaskRun.objects.all()
    authentication_classes = []


class CeleryAPIView(ViewSet):
    def list(self, request):
        inspector = app.control.inspect()
        redis_client = redis.Redis(
            host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=1
        )
        # list all celery tasks
        return Response(
            {
                "celery": inspector.registered_tasks(),
                "redis": redis_client.get("celery"),
            }
        )
