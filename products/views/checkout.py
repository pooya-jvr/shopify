from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from products.cart import Cart


@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect("cart_detail")
    return render(request, "cart/checkout.html", {"cart": cart})
