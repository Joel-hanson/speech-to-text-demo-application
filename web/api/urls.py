from rest_framework import routers

from .views import CeleryAPIView, TaskRunsAPIView, UploadAPIView

router = routers.DefaultRouter()
router.register(r"upload", UploadAPIView, basename="upload")
router.register(r"task-runs", TaskRunsAPIView, basename="task-runs")
router.register(r"celery", CeleryAPIView, basename="celery")

urlpatterns = router.urls
