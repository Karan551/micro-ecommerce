from django.forms import ModelForm
from .models import Product
from django import forms




class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_price", "product_slug"]

        labels = {
            "product_name": "Name:",
            "product_price": "Price:",
            "product_slug": "Slug:"
        }

        widgets = {
            "product_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter Product Name:",
                    "class": "form-control"
                }
            ),
            "product_price": forms.TextInput(attrs={
                "placeholder": "Enter Product Price:",
                "class": "form-control"
            }),
            "product_slug": forms.TextInput(attrs={
                "placeholder": "Enter Product Slug:",
                "class": "form-control"
            })

        }
