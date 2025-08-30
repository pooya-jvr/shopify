from django.shortcuts import render
from products.models import Product


def home(request):
    products = Product.objects.all()

    # گرفتن آیتم‌های سبد خرید از session
    cart = request.session.get(
        "cart", {}
    )  # cart یک dict با product_id: {name, price, quantity}

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

    return render(
        request,
        "core/home.html",
        {
            "products": products,
            "cart_items": cart_items,
        },
    )
