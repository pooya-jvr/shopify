from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.exceptions import APIException
from users.models import CustomUser, UserAddress
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


class GetUserPrifileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "is_superuser",
            "mobile_number",
            "date_joined",
        ]


class GetUserAddressSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserAddress
        fields = [
            "id",
            "user",
            "address",
            "floor",
            "building",
            "street",
            "city",
            "sub_city",
            "postal_code",
            "phone_number",
            "home_phone_number",
            "is_default",
            "created_at",
            "updated_at",
            "created_by",
        ]

    def get_user(self, obj):
        return obj.user.username
