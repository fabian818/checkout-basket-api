from rest_framework.routers import DefaultRouter
from .views import BasketViewSet, AssociationViewSet

router = DefaultRouter()
router.register(r'baskets', BasketViewSet, basename='basket')
router.register(r'associations', AssociationViewSet, basename='association')
urlpatterns = router.urls
