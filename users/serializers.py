from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.exceptions import APIException
from users.models import CustomUser
from rest_framework import serializers


class UsernameNotFound(APIException):
    status_code = 405
    default_detail = "این یوزرنیم وجود ندارد."
    default_code = "username_not_found"


class WrongPassword(APIException):
    status_code = 401
    default_detail = "پسورد اشتباه است."
    default_code = "wrong_password"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = CustomUser.USERNAME_FIELD

    def validate(self, attrs):
        username = attrs.get(self.username_field)
        password = attrs.get("password")

        if not CustomUser.objects.filter(**{self.username_field: username}).exists():
            raise UsernameNotFound()

        user = authenticate(username=username, password=password)
        if user is None:
            raise WrongPassword()

        data = super().validate(attrs)
        return data


class GetUserPrifileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=254)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    mobile_number = serializers.CharField(max_length=255)
