from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Association

@receiver(post_save, sender=Association)
def save_price(sender, instance, **kwargs):
    if kwargs['created'] is True:
        basket = instance.basket
        basket.total += instance.product.price
        basket.save()
