from django.urls import path


from .views import RegisterAPIView, ActivateAPIView, ChangePasswordAPIView, ForgotPasswordAPIView, \
    ForgotPasswordConfirmAPIView, UpdateUserAPIView, UserGetAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/', ActivateAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('change_password/', ChangePasswordAPIView.as_view()),
    path('forgot_password/', ForgotPasswordAPIView.as_view()),
    path('forgot_password_confirm/', ForgotPasswordConfirmAPIView.as_view()),
    path('update_user/', UpdateUserAPIView.as_view()),
    path('userinfo/', UserGetAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),


]