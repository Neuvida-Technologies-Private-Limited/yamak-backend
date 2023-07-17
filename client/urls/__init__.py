from client.urls import access
from client.urls import workspace
from client.urls import connector
from client.urls import ai_models

urlpatterns = []
urlpatterns += access.urlpatterns
urlpatterns += connector.urlpatterns
urlpatterns += workspace.urlpatterns
urlpatterns += ai_models.urlpatterns
