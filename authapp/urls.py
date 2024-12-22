from django.urls import path
from .views import RegisterView, LoginView, TokenRefreshView, UserDetailView, PasswordResetView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
