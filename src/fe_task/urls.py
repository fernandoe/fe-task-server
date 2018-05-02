from rest_framework import routers

from .views import TaskModelViewSet

router = routers.SimpleRouter()
router.register(r'', TaskModelViewSet)

urlpatterns = router.urls
