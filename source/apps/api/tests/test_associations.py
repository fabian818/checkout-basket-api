from json import dumps
from rest_framework.test import APITestCase
from rest_framework import status
from ..factories import BasketFactory, ProductFactory

BASE_LIST_PATH = '/api/associations/'

ASSOCIATION_PAYLOAD = {
    'basket_id': None,
    'product__code': 'PEN',
    'quantity': 1
}


class AddProductToBasketTest(APITestCase):
    """ Test module for POST to create associations API """

    def setUp(self):
        ProductFactory(code='PEN', price=5)
        ProductFactory(code='TSHIRT', price=20)
        ProductFactory(code='MUG', price=7.5)
        self.basket = BasketFactory()

    def test_create_association(self):
        associations_payload = ASSOCIATION_PAYLOAD.copy()
        associations_payload['basket_id'] = self.basket.id
        response = self.client.post(
                BASE_LIST_PATH,
                dumps(associations_payload),
                content_type="application/json")
        self.basket.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.basket.total, 5)
