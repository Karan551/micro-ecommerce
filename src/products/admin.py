from django.contrib import admin
from .models import Product, ProductAttachMent
# Register your models here.

admin.site.register((Product, ProductAttachMent))
