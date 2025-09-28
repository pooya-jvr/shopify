from django.db import models

from users.models import UserAddress


class Order(models.Model):

    ORDER_STATUS_CHOICES = (
        ("pending", "pending"),
        ("paid", "paid"),
        ("cancelled", "cancelled"),
        ("shipped", "shipped"),
        ("delivered", "delivered"),
        ("returned", "returned"),
        ("refunded", "refunded"),
    )

    user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="user_order"
    )
    address = models.ForeignKey(
        UserAddress, on_delete=models.CASCADE, related_name="order_address"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES)
    payment_status = models.CharField(max_length=10, default="pending")
    payment_id = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="created_by"
    )
    updated_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="updated_by"
    )
    cancel_request = models.BooleanField(default=False)
    cancel_reason = models.CharField(max_length=100, default="")
    cancel_at = models.DateTimeField(null=True, blank=True)
    cancel_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="cancel_by"
    )

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="order_items"
    )
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="created_by"
    )
    updated_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="updated_by"
    )

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity
