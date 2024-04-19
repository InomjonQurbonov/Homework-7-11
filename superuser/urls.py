from django.urls import path, include
from django.contrib.auth import views
from .views import (
    SendVerificationEmailView,
    RegisterAPIView,
    ChangePasswordView,
    RequestPasswordResetView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('reset_password/', RequestPasswordResetView.as_view(), name='reset_password'),
    path('send-verification-email/', SendVerificationEmailView.as_view(), name='send_verification_email'),
    path('register-api/', RegisterAPIView.as_view(), name='register_api'),
    path('request-password-reset/', RequestPasswordResetView.as_view(), name='request_password_reset'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('verify_email/', SendVerificationEmailView.as_view(), name='verify_email'),
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
