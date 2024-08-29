from django.urls import path
from .views import RegisterAPIView, ActivateAPIView, ChangePasswordAPIView, ForgotPasswordAPIView, \
    ForgotPasswordConfirmAPIView
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
    path('refresh', TokenRefreshView.as_view()),


]