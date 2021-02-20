from django.db import models


class DateTable(models.Model):
    '''
    MetaModel to save timestamp fields configuration
    '''
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Basket(DateTable):
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)


class Product(DateTable):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    '''
    code field should be indexed because of potential filter querys using this field
    '''
    indexes = [
       models.Index(fields=['code']),
    ]


class Association(DateTable):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False, default=1)
