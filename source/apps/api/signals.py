from decimal import Decimal
from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save
from .models import Association

PEN_CODE = 'PEN'
TSHIRT_CODE = 'TSHIRT'

def get_basket_total(associations_by_product):
    ''' Algorithm to get total price of basket including promos'''

    total = 0
    for product_group in associations_by_product:
        price = product_group['product__price']
        quantity = product_group['quantity_per_product']
        if product_group['product__code'] == PEN_CODE:
            # When product associated has PEN code (2x1 PROMO)'''
            total += price * int((quantity + 1) / 2)
        elif product_group['product__code'] == TSHIRT_CODE:
            # When product associated has TSHIRT code (0.25 off if 3 or more products) '''
            if quantity >= 3:
                total += price * quantity * Decimal(0.75)
            else:
                total += price * quantity
        else:
            total += price * quantity
    return total

@receiver(post_save, sender=Association)
def refresh_basket_total(sender, instance, **kwargs):
    ''' Signal triggered by product association to basket '''

    if kwargs['created'] is True:
        basket = instance.basket
        # get quantity of associations grouped by products
        associations_by_product = Association.objects.filter(
            basket=basket
        ).values(
            'product__code',
            'product__price'
        ).annotate(
            quantity_per_product=Sum('quantity')
        )
        basket.total = get_basket_total(associations_by_product)
        basket.save()
