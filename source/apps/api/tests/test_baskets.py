from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Basket, Association
from ..factories import BasketFactory, ProductFactory, AssociationFactory

BASE_LIST_PATH = '/api/baskets/'
BASE_DETAIL_PATH = '/api/baskets/{}/'


class CreateBasketTest(APITestCase):
    """ Test module for POST to create baskets API """
    def test_create_baskets(self):
        response = self.client.post(
                BASE_LIST_PATH)
        baskets_count = Basket.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(baskets_count, 1)



class GetSingleBasketTest(APITestCase):
    """ Test module for GET to retrieve single basket API """

    def setUp(self):
        self.basket = BasketFactory(total=20)

    def test_get_single_basket_with_amount(self):
        client = self.client
        response = client.get(
                BASE_DETAIL_PATH.format(self.basket.id))
        basket = Basket.objects.get(id=self.basket.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(basket.total), response.json()['total'])


class DeleteSingleBasketTest(APITestCase):
    """ Test module for DELETE to remove single basket API """

    def setUp(self):
        pen = ProductFactory(code='PEN', price=5)
        tshirt = ProductFactory(code='TSHIRT', price=20)
        mug = ProductFactory(code='MUG', price=7.5)
        self.basket = BasketFactory(total=32.5)
        AssociationFactory(basket=self.basket, product=pen)
        AssociationFactory(basket=self.basket, product=tshirt)
        AssociationFactory(basket=self.basket, product=mug)

    def test_get_single_basket_with_amount(self):
        client = self.client
        baskets_count = Basket.objects.all().count()
        associations_count = Association.objects.all().count()
        self.assertEqual(baskets_count, 1)
        self.assertEqual(associations_count, 3)
        response = client.delete(
                BASE_DETAIL_PATH.format(self.basket.id))
        baskets_count = Basket.objects.all().count()
        associations_count = Association.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(baskets_count, 0)
        self.assertEqual(associations_count, 0)
