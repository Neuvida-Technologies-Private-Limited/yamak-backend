from django.urls import path

from client.views import workspace

API_MODULE = 'workspace'

urlpatterns = [
    # path(f'{API_MODULE}/login', workspace.LoginView.as_view(), name='login'),
]
