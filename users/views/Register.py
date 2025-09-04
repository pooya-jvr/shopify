from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.forms import CustomUserCreationForm


class Register(APIView):
    def post(self, request):
        form = CustomUserCreationForm(request.data)
        if form.is_valid():
            form.save()
            return Response(
                {"message": "ثبت‌نام با موفقیت انجام شد"}, status=status.HTTP_201_CREATED
            )
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
