from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
# Create your models here.

PROTECTED_MEDIA_ROOT = settings.PROTECTED_MEDIA_ROOT
protected_storage = FileSystemStorage(location=str(PROTECTED_MEDIA_ROOT))


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)

    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=9.99)

    product_image = models.ImageField(
        upload_to="products/", blank=True, null=True)
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

        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return f"/products/{self.product_slug}"


def handle_product_attachment_upload(instance, filename):
    return f"products/{instance.product.product_slug}/attachments/{filename}"


class ProductAttachMent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # STRD
    file = models.FileField(upload_to=handle_product_attachment_upload,
                            storage=protected_storage)
    is_free = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
