from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list_view, name="product_list"),
    path("create/", views.product_create_view, name="create"),
    path("<slug:product_slug>", views.product_detail_view, name="product_detail"),

]
