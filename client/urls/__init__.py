from client.urls import access
from client.urls import workspace
from client.urls import connector

urlpatterns = []
urlpatterns += access.urlpatterns
urlpatterns += connector.urlpatterns
urlpatterns += workspace.urlpatterns
