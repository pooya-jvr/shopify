from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import GetUserPrifileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class ShowUserProfile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        serializer = GetUserPrifileSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
