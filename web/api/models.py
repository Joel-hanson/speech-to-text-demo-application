from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_results.models import TASK_STATE_CHOICES, TaskResult, states


class Upload(models.Model):
    file = models.FileField(upload_to="uploads/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # id
        return f"{self.pk} - {self.file.name}"


class TaskRun(models.Model):
    upload = models.ForeignKey(Upload, related_name="uploads", on_delete=models.CASCADE)
    task_id = models.CharField(max_length=255, default="", unique=True)
    text = models.TextField(default="")
    service = models.CharField(max_length=255, default="")
    status = models.CharField(
        max_length=255, choices=TASK_STATE_CHOICES, default="STARTED"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.upload.file.name} - {self.status}"


@receiver(post_save, sender=TaskResult)
def task_result_post_save(sender, instance, **kwargs):
    print("task_result_post_save", instance.status)
    if instance.status == states.FAILURE:
        try:
            task_run = TaskRun.objects.get(task_id=instance.task_id)
            task_run.status = states.FAILURE
            task_run.save()
            send_status_update(task_run)
        except TaskRun.DoesNotExist:
            return


from .utils import send_status_update
