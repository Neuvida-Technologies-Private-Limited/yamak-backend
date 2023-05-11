from django.shortcuts import get_object_or_404
from oauth2_provider.models import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from access.constants import OTPRequestType
from access.services import auth_service
from access.services import profile_service
from client.utils import access_util
from main.mixins import validations
from main.mixins.exceptions import BadRequestError
from main.mixins.exceptions import UnAuthorizedError
from main.mixins.views import APIResponse

class LoginView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)


class TokenView(APIView, APIResponse):
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


class LogoutView(APIView, APIResponse):
    """logout/revoke tokens"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        bearer_token = request.META.get('HTTP_AUTHORIZATION', None)
        if bearer_token:

            access_token = bearer_token.split()[1]

            # user token validation
            get_object_or_404(
                klass=AccessToken,
                user_id=request.user.id,
                token=access_token,
            )
            auth_service.revoke_token(
                user_id=request.user.id,
                access_token=access_token,
            )

        return self.get_success_response(json_response={'logged_out': True})

class SignUpAdminView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)

class SignUpUserView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)

class ForgetPasswordView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)


class AddUserView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)


class DeleteUserView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)

class GetProfileView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)

class EditProfileView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)

class DeleteAccountView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not password or validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user_email(email=email)

        if not user:
            raise BadRequestError('invalid user')
        if not user.check_password(password):
            raise BadRequestError('invalid password')

        tokens = auth_service.create_auth_tokens(user=user)

        response = {
            'access_token': tokens.get('access_token'),
            'refresh_token': tokens.get('refresh_token')
        }

        return self.get_success_response(json_response=response)

