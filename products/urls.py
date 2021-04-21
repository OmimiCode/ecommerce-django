from django.urls import path

from products import views

urlpatterns = [
    path("", views.create_product)
]