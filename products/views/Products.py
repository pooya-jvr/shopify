from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import Product
from products.serializers import GetProductsSerializer


class Products(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        products_obj = Product.objects.filter(stock=True)
        serz_data = GetProductsSerializer(
            products_obj, many=True, context={"request": request}
        )
        return Response(data=serz_data.data, status=status.HTTP_200_OK)
