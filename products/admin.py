from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "stock", "discount")
    list_filter = ("category", "stock")
    search_fields = ("name", "description")
    ordering = ("name",)
    readonly_fields = ("created_at", "updated_at")
