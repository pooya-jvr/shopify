from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import MyTokenObtainPairSerializer


class Login(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
