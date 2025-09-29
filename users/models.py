from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username


class UserAddress(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="address"
    )
    address = models.CharField(max_length=100, blank=True, null=True)
    floor = models.CharField(max_length=100, blank=True, null=True)
    building = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    sub_city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    home_phone_number = models.CharField(max_length=100, blank=True, null=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="address_created_by"
    )
    updated_by = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="address_updated_by"
    )
