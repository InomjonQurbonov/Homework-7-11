import random
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import View
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .forms import RegistrationForm, LoginForm
from .serializers import UserSerializer, ChangePasswordSerializer


class SendVerificationEmailView(View):
    def get(self, request):
        return render(request, 'registration/confirm_mail.html')

    def post(self, request):
        email = request.POST.get('email')
        verification_code = random.randint(100000, 999999)
        user = get_user_model().objects.get(email=email)
        user.profile.verification_code = verification_code
        user.profile.save()
        email_subject = 'Your email verification code'
        email_body = f'Your verification code is: {verification_code}'
        send_mail(email_subject, email_body, 'your-email@example.com', [email])
        return render(request, 'registration/confirm_send_email.html')


class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=request.user.username, password=serializer.validated_data['old_password'])
            if user:
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return JsonResponse({'status': 'success', 'message': 'Password changed successfully.'})
            else:
                return JsonResponse({'error': 'Wrong password.'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return JsonResponse({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_user_model().objects.filter(email=email).first()
        if not user:
            return JsonResponse({'error': 'Email not found.'}, status=status.HTTP_400_BAD_REQUEST)

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)

        reset_url = f'http://127.0.0.1:8000/password-reset/{token}/{user.pk}/'
        email_html_content = render_to_string('registration/password_reset_email.html', {'reset_url': reset_url})

        send_mail('Password Reset', '', 'from@example.com', [email], html_message=email_html_content)

        return JsonResponse({'message': 'Password reset email sent.'})
