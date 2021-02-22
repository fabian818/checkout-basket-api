from json import dumps
from django.test import TestCase
from rest_framework import status
from ..factories import BasketFactory, ProductFactory

BASE_LIST_PATH = '/api/associations/'
ASSOCIATION_PAIRS = [
    {
        'associations': [
            {
                'basket_id': None,
                'product__code': 'PEN',
                'quantity': 1
            },
            {
                'basket_id': None,
                'product__code': 'TSHIRT',
                'quantity': 1
            },
            {
                'basket_id': None,
                'product__code': 'MUG',
                'quantity': 1
            }
        ],
        'total':  32.50
    },
    {
        'associations': [
            {
                'basket_id': None,
                'product__code': 'PEN',
                'quantity': 2
            },
            {
                'basket_id': None,
                'product__code': 'TSHIRT',
                'quantity': 1
            }
        ],
        'total':  25
    },
    {
        'associations': [
            {
                'basket_id': None,
                'product__code': 'PEN',
                'quantity': 1
            },
            {
                'basket_id': None,
                'product__code': 'TSHIRT',
                'quantity': 2
            },
            {
                'basket_id': None,
                'product__code': 'TSHIRT',
                'quantity': 2
            }
        ],
        'total':  65
    },
    {
        'associations': [
            {
                'basket_id': None,
                'product__code': 'PEN',
                'quantity': 3
            },
            {
                'basket_id': None,
                'product__code': 'TSHIRT',
                'quantity': 3
            },
            {
                'basket_id': None,
                'product__code': 'MUG',
                'quantity': 1
            }
        ],
        'total':  62.5
    }
]


class AddProductToBasketTestTotalAmount(TestCase):
    """ Test module for POST to create associations API """

    def setUp(self):
        ProductFactory(code='PEN', price=5)
        ProductFactory(code='TSHIRT', price=20)
        ProductFactory(code='MUG', price=7.5)

    def test_create_association(self):
        client = self.client
        for associations_pair in ASSOCIATION_PAIRS:
            basket = BasketFactory()
            for association in associations_pair['associations']:
                association['basket_id'] = basket.id
                response = client.post(
                        BASE_LIST_PATH,
                        dumps(association),
                        content_type="application/json")
            basket.refresh_from_db()
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(basket.total, associations_pair['total'])
