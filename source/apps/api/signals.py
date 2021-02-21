from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save
from .models import Association

PEN_CODE = 'PEN'
TSHIRT_CODE = 'TSHIRT'

@receiver(post_save, sender=Association)
def save_price(sender, instance, **kwargs):
    if kwargs['created'] is True:
        basket = instance.basket
        associations_by_product = Association.objects.filter(
            basket=basket
        ).values(
            'product__code',
            'product__price'
        ).annotate(
            quantity_per_product=Sum('quantity')
        )
        basket.total = 0
        for product_group in associations_by_product:
            price = product_group['product__price']
            quantity = product_group['quantity_per_product']
            if product_group['product__code'] == PEN_CODE:
                basket.total += price * quantity
            elif product_group['product__code'] == PEN_CODE:
                basket.total += price * quantity
            else:
                basket.total += price * quantity
        basket.save()
