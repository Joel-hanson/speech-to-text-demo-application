from django.conf import settings
from django.shortcuts import render
from kafka import KafkaProducer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Upload
from .serializers import UploadSerializer


# Create your views here.
class UploadAPIView(ModelViewSet):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(settings.INTERNAL_BOOTSTRAP_SERVERS)
        producer = KafkaProducer(bootstrap_servers=settings.INTERNAL_BOOTSTRAP_SERVERS)
        message = serializer.data
        message_string = str(message)
        message_bytes = message_string.encode("utf-8")
        producer.send("test", message_bytes)
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
