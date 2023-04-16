from backend.celery import app
from django.conf import settings
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
    queryset = Upload.objects.order_by("created_at")
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        task_run = create_task_run(serializer.data["id"])
        send_status_update(TaskRunsDetailedSerializer(task_run).data)
        headers = self.get_success_headers(serializer.data)
        app.autodiscover_tasks()
        task = app.signature(
            "speech-service.SpeechRecognition",
            args=[
                task_run.id,  # type: ignore
                serializer.data["file"],
                serializer.data["created_at"],
                serializer.data["updated_at"],
            ],
        ).apply_async()
        if task:
            task_run.status = "PROCESSING"
            task_run.save()
            task_run_data = TaskRunsDetailedSerializer(task_run).data
            send_status_update(task_run_data)
        else:
            task_run.status = "FAILURE"
            task_run.save()
            task_run_data = TaskRunsDetailedSerializer(task_run).data
            send_status_update(task_run_data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    # def perform_create(self, serializer):
    #     serializer.save()

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop("partial", False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     if getattr(instance, "_prefetched_objects_cache", None):
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)

    # def perform_update(self, serializer):
    #     serializer.save()

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def perform_destroy(self, instance):
    #     instance.delete()

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def partial_update(self, request, *args, **kwargs):
    #     kwargs["partial"] = True
    #     return self.update(request, *args, **kwargs)

    @action(detail=False, methods=["get"], url_path="detailed")
    def detailed(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UploadDetailedSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="task_runs")
    def task_runs(self, request, *args, **kwargs):
        queryset = TaskRun.objects.all()
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
