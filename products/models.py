from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="products/images/", null=True, blank=True)
    category = models.CharField(max_length=100)
    discount = models.PositiveIntegerField(default=0)
    stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="created_by"
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="updated_by"
    )
    sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = 0
        for product in self.product_set.all():
            total += product.price
        return total

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product"
    )
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name
