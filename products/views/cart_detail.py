from django.shortcuts import render


def cart_detail(request):
    cart = request.session.get("cart", {})

    cart_items = []
    for product_id, item in cart.items():
        cart_items.append(
            {
                "id": product_id,
                "name": item["name"],
                "price": item["price"],
                "quantity": item["quantity"],
            }
        )

    return render(request, "products/cart.html", {"cart_items": cart_items})
