from django.shortcuts import get_object_or_404
from oauth2_provider.models import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from workspace.services import workspace_service
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

    def post(self, request):

        payload: dict = request.data
        
        id = payload.get('id', None)
        if not id:
            raise BadRequestError('invalid id')

        # get user
        user = request.user

        workspace_service.delete_workspace(user, id)

        response = {
            "workspace_created": True
        }

        return self.get_success_response(json_response=response)


class EditWorkspaceView(APIView, APIResponse):
    """Refresh a token"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        payload: dict = request.data
        
        id = payload.get('id', None)
        if not id:
            raise BadRequestError('invalid id')

        # get user
        user = request.user

        workspace_service.delete_workspace(user, id)

        response = {
            "workspace_created": True
        }

        return self.get_success_response(json_response=response)


class GetWorkspaceView(APIView, APIResponse):
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


class GetExperimentInfoView(APIView, APIResponse):
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


class EditExperimentView(APIView, APIResponse):
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
        

class DeleteExperimentView(APIView, APIResponse):
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
