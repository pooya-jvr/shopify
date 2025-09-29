from django.contrib import admin
from users.models import CustomUser, UserAddress


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "mobile_number",
        "sex",
        "is_active",
        "is_staff",
    )
    search_fields = ("username", "email", "mobile_number")
    list_filter = ("is_active", "is_staff", "sex")


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "address",
        "city",
        "sub_city",
        "postal_code",
        "is_default",
    )
    search_fields = ("address", "city", "postal_code", "phone_number")
    list_filter = ("is_default", "city")
