from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)

    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=9.99)

    og_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=9.99)

    stripe_price = models.IntegerField(default=999)
    product_slug = models.SlugField(unique=True)
    price_changed_timestamp = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.product_price != self.og_price:
            self.og_price = self.product_price

            self.stripe_price = int(self.product_price*100)
            self.price_changed_timestamp = timezone.now()

        super.save(*args, **kwargs)
