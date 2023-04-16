from django.contrib import admin

from .models import TaskRun, Upload

admin.site.register(Upload)
admin.site.register(TaskRun)
