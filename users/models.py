from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
