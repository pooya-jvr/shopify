from django.urls import path
from users import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = []
