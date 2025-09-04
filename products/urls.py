from django.urls import path
from products import views


urlpatterns = [
    path("products/", views.Products.as_view(), name="products"),
]
