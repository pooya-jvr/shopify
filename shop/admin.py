from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "address",
        "status",
        "payment_status",
        "total_price",
        "is_active",
        "cancel_request",
        "cancel_reason",
        "created_at",
    )
    search_fields = ("user__username", "payment_id", "cancel_reason")
    list_filter = ("status", "payment_status", "is_active", "cancel_request")
    autocomplete_fields = ("user", "address", "created_by", "updated_by", "cancel_by")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "total_price", "created_at")
    search_fields = ("product__name", "order__user__username")
    autocomplete_fields = ("order", "product", "created_by", "updated_by")
