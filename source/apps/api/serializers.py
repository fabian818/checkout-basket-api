from rest_framework import serializers
from .models import Basket, Association


class BasketSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)
    class Meta:
        model = Basket
        fields = '__all__'

class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = '__all__'
