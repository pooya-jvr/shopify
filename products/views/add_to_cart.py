# products/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from products.models import Product


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1
    else:
        cart[str(product_id)] = {
            "name": product.name,
            "price": float(product.price),
            "quantity": 1,
        }

    request.session["cart"] = cart
    request.session.modified = True

    total_items = sum(item["quantity"] for item in cart.values())
    return JsonResponse({"success": True, "total_items": total_items})
