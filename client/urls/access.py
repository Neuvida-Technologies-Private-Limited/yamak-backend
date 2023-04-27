from django.urls import path

from client.views import access

API_MODULE = 'access'

urlpatterns = [
    path(f'{API_MODULE}/otp', access.OTPView.as_view(), name='otp'),
    path(f'{API_MODULE}/token', access.TokenView.as_view(), name='token'),
    path(f'{API_MODULE}/logout', access.LogoutView.as_view(), name='logout'),
]
