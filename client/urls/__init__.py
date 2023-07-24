from client.urls import access
from client.urls import ticket

urlpatterns = []
urlpatterns += access.urlpatterns
urlpatterns += ticket.urlpatterns
