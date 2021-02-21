from rest_framework import mixins, viewsets
from .serializers import BasketSerializer, AssociationSerializer
from .models import Basket, Association

class BasketViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()


class AssociationViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = AssociationSerializer
    queryset = Association.objects.all()
