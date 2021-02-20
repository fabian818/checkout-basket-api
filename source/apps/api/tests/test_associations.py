from json import dumps
from django.test import TestCase
from rest_framework import status
from ..factories import BasketFactory, ProductFactory

BASE_LIST_PATH = '/api/associations/'
BASE_DETAIL_PATH = '/api/associations/{}'

ASSOCIATION_PAYLOAD = {
    'basket_id': None,
    'product__code': 'PEN',
    'quantity': 1
}


class AddProductToBasketTest(TestCase):
    """ Test module for POST to create baskets API """

    def setUp(self):
        ProductFactory(code='PEN', price=5)
        ProductFactory(code='TSHIRT', price=20)
        ProductFactory(code='MUG', price=7.5)
        self.basket = BasketFactory()

    def test_create_association(self):
        client = self.client
        associations_payload = ASSOCIATION_PAYLOAD.copy()
        associations_payload['basket_id'] = self.basket.id
        response = client.post(
                BASE_LIST_PATH,
                dumps(associations_payload),
                content_type="application/json")
        self.basket.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.basket.amount, 5)
