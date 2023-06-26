from django.urls import path

from client.views import workspace

API_MODULE = 'workspace'

urlpatterns = [
    # workspace endpoints
    path(f'{API_MODULE}/create_workspace', workspace.CreateWorkspaceView.as_view(), name='create_workspace'),
    path(f'{API_MODULE}/delete_workspace', workspace.DeleteWorkspaceView.as_view(), name='delete_workspace'),
    path(f'{API_MODULE}/edit_workspace', workspace.EditWorkspaceView.as_view(), name='edit_workspace'),
    path(f'{API_MODULE}/get_workspace_info', workspace.GetWorkspaceView.as_view(), name='get_workspace_info'),

    # experiment endpoints
    path(f'{API_MODULE}/create_experiment', workspace.CreateExperimentView.as_view(), name='create_experiment'),
    path(f'{API_MODULE}/edit_experiment', workspace.EditExperimentView.as_view(), name='edit_experiment'),
    path(f'{API_MODULE}/delete_experiment', workspace.DeleteExperimentView.as_view(), name='delete_experiment'),
]  
