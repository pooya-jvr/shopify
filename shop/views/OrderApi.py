from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from shop.models import Order, OrderItem
from shop.serializers import OrderSerializer, CreateOrderSerializer
from products.models import Cart


class OrderApi(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        JWTAuthentication,
    ]

    def get(self, request):
        order = Order.objects.filter(user=request.user, is_active=True)

        if order:
            serializer = OrderSerializer(order, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND
        )

    def post(self, request):
        order, created = Order.objects.get_or_create(
            user=request.user,
            is_active=True,
            defaults={"status": "draft"},
        )
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        if not cart_items:
            return Response(
                {"message": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST
            )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                created_by=request.user,
                updated_by=request.user,
            )

        cart.items.all().delete()

        serializer = CreateOrderSerializer(order, context={"request": request})

        return Response(
            {"message": "Order finalized successfully", "order": serializer.data},
            status=status.HTTP_200_OK,
        )
