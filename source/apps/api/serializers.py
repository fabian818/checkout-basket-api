from rest_framework import serializers
from .models import Basket, Association, Product


class BasketSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)
    class Meta:
        model = Basket
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AssociationSerializer(serializers.ModelSerializer):
    product__code = serializers.CharField(write_only=True, required=True)
    product_id = serializers.IntegerField(read_only=True)
    basket_id = serializers.IntegerField()

    def create(self, validated_data):
        product = Product.objects.get(code=validated_data['product__code'])
        del validated_data['product__code']
        association = Association.objects.create(product_id=product.id, **validated_data)
        return association

    class Meta:
        model = Association
        exclude = ('product', 'basket')
