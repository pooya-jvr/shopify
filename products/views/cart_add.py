from django.shortcuts import redirect, get_object_or_404
from products.cart import Cart
from products.models import Product


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect("cart_detail")
