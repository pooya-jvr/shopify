from products.models import Category
from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializers import GetAllCategorys
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class GetCategorys(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        all_categorys = Category.objects.filter(is_active=True)

        if all_categorys:
            serz_data = GetAllCategorys(all_categorys, many=True)

        return Response(serz_data.data, status=status.HTTP_200_OK)
