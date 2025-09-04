from django.urls import path
from users import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("login/", views.Login.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user-profile/", views.ShowUserProfile.as_view(), name="show_user_profile"),
    path("get-csrf/", views.get_csrf, name="get_csrf"),
]
