from django.shortcuts import get_object_or_404
from oauth2_provider.models import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from workspace.services import workspace_service, experiment_service
from client.utils import access_util
from main.mixins import validations
from main.mixins.exceptions import BadRequestError
from main.mixins.exceptions import UnAuthorizedError
from main.mixins.views import APIResponse

class CreateWorkspaceView(APIView, APIResponse):
    """Create a workspace"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        payload: dict = request.data
        
        name = payload.get('name', None)
        if not name:
            raise BadRequestError('invalid name')

        # get user
        user = request.user

        workspace_service.create_workspace(user, name)

        response = {
            "workspace_created": True
        }

        return self.get_success_response(json_response=response)


class DeleteWorkspaceView(APIView, APIResponse):
    """Delete a workspace"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request):

        payload: dict = request.data
        
        id = payload.get('id', None)
        if not id:
            raise BadRequestError('invalid id')

        # get user
        user = request.user

        workspace_service.delete_workspace(user, id)

        response = {
            "workspace_deleted": True
        }

        return self.get_success_response(json_response=response)


class EditWorkspaceView(APIView, APIResponse):
    """Refresh a token"""

    permission_classes = (IsAuthenticated,)

    def put(self, request):

        payload: dict = request.data
        
        id = payload.get('id', None)
        if not id:
            raise BadRequestError('invalid id')

        name = payload.get('name', None)
        if not name:
            raise BadRequestError('invalid name')

        # get user
        user = request.user

        workspace_service.edit_workspace(user, id, name)

        response = {
            "workspace_created": True
        }

        return self.get_success_response(json_response=response)


class GetWorkspaceView(APIView, APIResponse):
    """Refresh a token"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        payload: dict = request.data

        # get user
        user = request.user

        response = workspace_service.get_workspace_info(user)

        return self.get_success_response(json_response=response)


class ShareWorkspaceView(APIView, APIResponse):
    """Refresh a token"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        payload: dict = request.data
        refresh_token = payload.get('refresh_token', None)
        if not refresh_token:
            raise UnAuthorizedError(message='invalid refresh token')

        access_token = payload.get('access_token', None)
        if not access_token:
            raise UnAuthorizedError(message='invalid access token')

        auth_tokens = auth_service.refresh_new_token(
            refresh_token=refresh_token,
            access_token=access_token,
        )
        return self.get_success_response(json_response=auth_tokens)


class CreateExperimentView(APIView, APIResponse):
    """Refresh a token"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        payload: dict = request.data

        workspace_id = payload.get('workspace_id', None)
        if not workspace_id:
            raise BadRequestError('invalid workspace_id')

        name = payload.get('name', None)
        if not name:
            raise BadRequestError('invalid name')

        # get user
        user = request.user

        experiment_service.create_experiment(user, workspace_id, name)

        response = {
            "experiment_created": True
        }

        return self.get_success_response(json_response=response)


class EditExperimentView(APIView, APIResponse):
    """Edit an experiment"""

    permission_classes = (IsAuthenticated,)

    def put(self, request):

        payload: dict = request.data
        
        experiment_id = payload.get('experiment_id', None)
        if not experiment_id:
            raise BadRequestError('invalid experiment_id')

        workspace_id = payload.get('workspace_id', None)
        if not workspace_id:
            raise BadRequestError('invalid workspace_id')

        name = payload.get('name', None)
        if not name:
            raise BadRequestError('invalid name')

        # get user
        user = request.user

        experiment_service.delete_experiment(user, workspace_id, experiment_id, name)

        response = {
            "experiment_edited": True
        }

        return self.get_success_response(json_response=response)
        

class DeleteExperimentView(APIView, APIResponse):
    """Delete an experiment"""

    permission_classes = (IsAuthenticated,)

    def delete(self, request):

        payload: dict = request.data
        
        experiment_id = payload.get('experiment_id', None)
        if not experiment_id:
            raise BadRequestError('invalid experiment_id')

        workspace_id = payload.get('workspace_id', None)
        if not workspace_id:
            raise BadRequestError('invalid workspace_id')

        # get user
        user = request.user

        experiment_service.delete_experiment(user, workspace_id, experiment_id)

        response = {
            "experiment_deleted": True
        }

        return self.get_success_response(json_response=response)
