from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [
    path("start/", views.purchase_start_view, name="start"),
    path("stop/", views.purchase_stop_view, name="stop"),
    path("success/", views.purchase_success_view, name="success"),
]
