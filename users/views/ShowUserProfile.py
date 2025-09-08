from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import GetUserPrifileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

import jdatetime


class ShowUserProfile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        serializer = GetUserPrifileSerializer(user)

        date_joined_shamsi = jdatetime.datetime.fromgregorian(
            datetime=user.date_joined
        ).strftime("%Y-%m-%d")

        data = {
            "date_joined": date_joined_shamsi,
        }
        response_data = {**serializer.data, **data}

        return Response(data=response_data, status=status.HTTP_200_OK)
