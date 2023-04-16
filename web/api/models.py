from django.db import models


class Upload(models.Model):
    file = models.FileField(upload_to="uploads/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # id
        return f"{self.pk} - {self.file.name}"


class TaskRun(models.Model):
    STATUS_CHOICES = (
        ("STARTED", "STARTED"),
        ("PROCESSING", "PROCESSING"),
        ("COMPLETED", "COMPLETED"),
        ("FAILURE", "FAILURE"),
    )
    upload = models.ForeignKey(Upload, related_name="uploads", on_delete=models.CASCADE)
    text = models.TextField(default="")
    service = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="STARTED")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
