from client.urls import access
from client.urls import workspace
from client.urls import user

urlpatterns = []
urlpatterns += access.urlpatterns
urlpatterns += workspace.urlpatterns
urlpatterns += user.urlpatterns
