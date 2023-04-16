from rest_framework import serializers

from .models import TaskRun, Upload


class TaskRunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRun
        fields = "__all__"


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"


class UploadDetailedSerializer(serializers.ModelSerializer):
    uploads = TaskRunsSerializer(many=True)

    class Meta:
        model = Upload
        fields = (
            "id",
            "file",
            "created_at",
            "updated_at",
            "uploads",
        )


class TaskRunsDetailedSerializer(serializers.ModelSerializer):
    upload = UploadSerializer()
    title = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    class Meta:
        model = TaskRun
        fields = (
            "id",
            "text",
            "service",
            "status",
            "date",
            "time",
            "title",
            "upload",
        )

    def get_title(self, obj):
        # get file name as title
        return obj.upload.file.name.split("/")[-1]

    def get_date(self, obj):
        # February 10, 2021
        return obj.upload.created_at.strftime("%B %d, %Y")

    def get_time(self, obj):
        # 10:00 PM
        return obj.upload.created_at.strftime("%I:%M %p")
