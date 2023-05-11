from django.urls import path

from client.views import user

API_MODULE = 'user'

urlpatterns = [
    # path(f'{API_MODULE}/login', user.LoginView.as_view(), name='login'),
]
