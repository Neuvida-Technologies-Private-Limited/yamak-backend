from django.urls import path

from client.views import access

from access.services import sentry_service

API_MODULE = 'access'

urlpatterns = [
    # sentry testing path
    path('/sentry-debug', sentry_service.trigger_error, name='sentry-debug'),
    
    # Access views
    path(f'{API_MODULE}/login', access.LoginView.as_view(), name='login'),
    path(f'{API_MODULE}/logout', access.LogoutView.as_view(), name='logout'),
    path(f'{API_MODULE}/refresh_token', access.TokenView.as_view(), name='refresh_token'),
    path(f'{API_MODULE}/sign_up', access.SignUpView.as_view(), name='sign_up_admin'),
    path(f'{API_MODULE}/forget_password', access.ForgetPasswordView.as_view(), name='forget_password'),

    # Admin views
    path(f'{API_MODULE}/delete_user', access.DeleteUserView.as_view(), name='delete_user'),

    # Profile views
    path(f'{API_MODULE}/get_profile', access.GetProfileView.as_view(), name='get_profile'),
    path(f'{API_MODULE}/edit_profile', access.EditProfileView.as_view(), name='edit_profile'),
]
