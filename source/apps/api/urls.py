from rest_framework.routers import DefaultRouter
from .views import BasketViewSet

router = DefaultRouter()
router.register(r'baskets', BasketViewSet, basename='basket')
urlpatterns = router.urls
