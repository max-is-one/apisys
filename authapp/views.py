from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, PasswordResetSerializer
from django.core.mail import send_mail
from rest_framework.response import Response

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class TokenRefreshView(TokenRefreshView):
    pass

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
        if user:
            #Sending email with link
            send_mail(
                'Password Reset Request',
                'Here is the link to reset your password: http://example.com/reset-password/',
                'from@example.com',
                [email],
                fail_silently=False,
            )
        return Response({"message": "If the email is registered, you will receive a password reset link."}, status=status.HTTP_200_OK)