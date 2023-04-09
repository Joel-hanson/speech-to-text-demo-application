from rest_framework import routers

from .views import UploadAPIView

router = routers.DefaultRouter()
router.register(r"upload", UploadAPIView, basename="upload")

urlpatterns = router.urls
