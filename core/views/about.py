from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def about(request):
    phone = "021-33810940"
    email = "blackrose@gmail.com"
    address = "خیابان راه آباد مرکزی ۱۳۷۱۰ شماره ۱۳۹۴۸"
    website = "https://black-rose.github.io/"

    return render(
        request,
        "core/about.html",
        {"phone": phone, "email": email, "address": address, "website": website},
    )
