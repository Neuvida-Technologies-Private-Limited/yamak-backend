from django.urls import path

from client.views import access

API_MODULE = 'access'

urlpatterns = [
    # path(f'{API_MODULE}/otp', access.OTPView.as_view(), name='otp'),
    # path(f'{API_MODULE}/token', access.TokenView.as_view(), name='token'),
    path(f'{API_MODULE}/login', access.LoginView.as_view(), name='login'),
    path(f'{API_MODULE}/logout', access.LogoutView.as_view(), name='logout'),
    path(f'{API_MODULE}/refresh_token', access.TokenView.as_view(), name='refresh_token'),
    # Todo implement these
    # path(f'{API_MODULE}/sign_up_admin', access.SignUpAdminView.as_view(), name='sign_up_admin'),
    # path(f'{API_MODULE}/sign_up_user', access.SignUpUserView.as_view(), name='sign_up_user'),
    # path(f'{API_MODULE}/forget_password', access.ForgetPasswordView.as_view(), name='forget_password')
]
