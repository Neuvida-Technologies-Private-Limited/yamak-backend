from client.urls import access
from client.urls import workspace

urlpatterns = []
urlpatterns += access.urlpatterns
urlpatterns += workspace.urlpatterns
urlpatterns += user.urlpatterns
