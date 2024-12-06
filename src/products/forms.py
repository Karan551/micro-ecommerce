from django.forms import ModelForm, modelformset_factory, inlineformset_factory
from .models import Product, ProductAttachMent
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


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_price",
                  "product_image", "product_slug"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ProductAttachMentForm(ModelForm):
    class Meta:
        model = ProductAttachMent
        fields = ["file", "name", "is_free", "active"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:

            if field in ["is_free", "active"]:
                continue
            self.fields[field].widget.attrs["class"] = "form-control"


# we can do withour fields attribute because it is modelForm
ProductAttachMentModelFormSet = modelformset_factory(
    ProductAttachMent,
    form=ProductAttachMentForm,
    fields=["file", "name", "is_free", "active"],
    extra=0,
    can_delete=False,

)

# ProductAttachMentInlineFormSet = inlineformset_factory(
#     Product,
#     ProductAttachMent,
#     ProductAttachMentForm,
#     formset=ProductAttachMentModelFormSet,
#     fields=["file", "name", "is_free", "active"],
#     can_delete=False,
#     extra=0
# )


ProductAttachmentInlineFormSet = inlineformset_factory(
    Product,
    ProductAttachMent,
    form = ProductAttachMentForm,
    formset = ProductAttachMentModelFormSet,
    fields = ['file', 'name','is_free', 'active'],
    extra=0,
    can_delete=False
)