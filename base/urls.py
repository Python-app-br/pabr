from rest_framework.routers import DefaultRouter
from base.views import ArtigosViewSet


app_name = 'base'

router = DefaultRouter(trailing_slash=False)
router.register(r'art', ArtigosViewSet)

urlpatterns = router.urls