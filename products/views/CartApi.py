from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from products.models import Cart, CartItem
from products.serializers import CartItemSerializer


class CartApi(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        items = cart.items.all()
        serializer = CartItemSerializer(items, many=True)
        total = sum([item.product.price * item.quantity for item in items])
        return Response(
            {"items": serializer.data, "total_price": total}, status=status.HTTP_200_OK
        )

    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product_id=product_id,
            defaults={"quantity": quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        items = cart.items.all()
        serializer = CartItemSerializer(items, many=True)
        total = sum(item.product.price * item.quantity for item in items)

        return Response({"items": serializer.data, "total_price": total}, status=200)


    def delete(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        data = request.data
        product_id = data.get("product_id")
        quantity = data.get("quantity")

        if quantity:
            quantity = int(quantity)
        else:
            quantity = 0

        product = CartItem.objects.filter(cart=cart, product_id=product_id)

        if not product or not product_id:
            return Response(
                {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if product and quantity == 0:
            product = product[0]
            product.delete()

            serializer = CartItemSerializer(product)
            total = sum(
                [item.product.price * item.quantity for item in cart.items.all()]
            )
            return Response(
                {"items": serializer.data, "total_price": total},
                status=status.HTTP_200_OK,
            )
        if product and quantity > 0:
            product = product[0]
            product.quantity -= quantity
            product.save()
            serializer = CartItemSerializer(product)
            total = sum(
                [item.product.price * item.quantity for item in cart.items.all()]
            )
            return Response(
                {"items": serializer.data, "total_price": total},
                status=status.HTTP_200_OK,
            )
