from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list_view, name="product_list"),
    path("create/", views.product_create_view, name="create"),
    path("<slug:product_slug>/", views.product_detail_view, name="product_detail"),
    path("<slug:product_slug>/download/<int:pk>",
         views.product_attachment_download_view, name="attachment_download"),

    path("<slug:product_slug>/manage/",
         views.product_manage_detail_view, name="manage"),
]
