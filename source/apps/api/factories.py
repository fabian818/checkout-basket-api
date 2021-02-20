import factory
from .models import Basket, Product, Association


class BasketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Basket

    total = 0


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    code = "PEN"
    name = "Lana PEN"
    price = 5


class AssociationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Association

    basket = factory.SubFactory(BasketFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 1
