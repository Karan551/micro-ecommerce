from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    completed = models.BooleanField(default=False)
    product_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
