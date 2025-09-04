from django.urls import path
from products import views


urlpatterns = [
    path("products/", views.Products.as_view(), name="products"),
    path("all-categorys/", views.GetCategorys.as_view(), name="get_all_category"),
]
