from rest_framework import mixins, viewsets
from .serializers import BasketSerializer
from .models import Basket

class BasketViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
