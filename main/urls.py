from django.urls import include
from django.urls import path

urlpatterns = [
    path('v1/client/', include('client.urls')),
]
