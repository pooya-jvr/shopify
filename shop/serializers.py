from rest_framework.exceptions import APIException
from shop.models import Order, OrderItem
from users.models import UserAddress
from rest_framework import serializers


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = [
            "id",
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
        ]


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    address = UserAddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "address",
            "created_at",
            "total_price",
            "status",
            "payment_status",
            "payment_id",
        ]

    def get_user(self, obj):
        return obj.user.username


class CreateOrderSerializer(serializers.ModelSerializer):
    address_id = serializers.IntegerField(write_only=True)

    def validate_address_id(self, value):
        user = self.context["request"].user
        try:
            address = UserAddress.objects.get(id=value, user=user)
        except UserAddress.DoesNotExist:
            raise serializers.ValidationError("Invalid address for this user")
        return address

    def update(self, instance, validated_data):
        address = validated_data.pop("address_id")
        instance.address = address
        instance.is_active = False
        instance.status = "pending"
        instance.save()
        return instance