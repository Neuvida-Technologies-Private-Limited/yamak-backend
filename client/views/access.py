from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from oauth2_provider.models import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import json

from access.constants import OTPRequestType
from access.services import auth_service
from access.services import profile_service
from client.utils import access_util
from main.mixins import validations
from main.mixins.exceptions import BadRequestError
from main.mixins.exceptions import UnAuthorizedError
from main.mixins.views import APIResponse

from access.models import User
from access.constants import UserType

class LoginView(APIView, APIResponse):
    """Generate and verifying token for consumer via password"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        password = payload.get('password', None)
        if not validations.is_valid_password(password):
            raise BadRequestError(message='invalid password')

        user = profile_service.get_user(email=email)

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

class SignUpView(APIView, APIResponse):
    """Add user vis generating and verifying otp"""

    def post(self, request):

        payload: dict = request.data

        request_type = payload.get('request_type', None)
        if not request_type:
            raise BadRequestError(message='invalid request type')

        email = payload.get('email', None)
        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')
            
        # generate otp for signup
        if request_type == OTPRequestType.GENERATE:

            user = profile_service.get_user(email=email)
            
            # raise error if user already exists
            if user:
                raise BadRequestError('user already exists')
            
            password = payload.get('password', None)

            if not validations.is_valid_password(password):
                raise BadRequestError(message='invalid password')

            first_name = payload.get('first_name', None)
            if not first_name:
                raise BadRequestError(message='invalid first_name')

            last_name = payload.get('last_name', None)
            if not last_name:
                raise BadRequestError(message='invalid last_name')

            user_type = payload.get('user_type', None)
            if not user_type or (user_type != UserType.ADMIN and user_type != UserType.USER):
                raise BadRequestError('invalid user_type')

            # create user
            user = profile_service.create_user(email, password, first_name, last_name, user_type)

            # Generate and send otp
            otp = access_util.generate_otp(
                email=email,
            )
            access_util.send_otp(email=email, otp=otp)

            response = {
                "otp_generated": True
            }

        elif request_type == OTPRequestType.VERIFY:

            otp = payload.get('otp', None)

            if not otp:
                raise BadRequestError(message='invalid otp')
            
            response = access_util.verify_otp(
                email=email,
                otp=otp
            )

            # validate user
            User.objects.filter(email=email).update(is_validated=True)

        else:
            raise BadRequestError('invalid request type')

        return self.get_success_response(json_response=response)

class ForgetPasswordView(APIView, APIResponse):
    """Update the password of the user"""

    def post(self, request):

        payload: dict = request.data
        email = payload.get('email', None)

        if not validations.is_valid_email(email):
            raise BadRequestError(message='invalid email')

        user = profile_service.get_user(email=email)

        if not user:
            raise BadRequestError('invalid user')
        
        request_type = payload.get('request_type', None)
        if request_type == OTPRequestType.GENERATE:

            # Generate and send otp
            otp = access_util.generate_otp(
                email=email,
            )
            
            access_util.send_otp(email=email, otp=otp)
            
            response = {
                "otp_generated": True
            }

        elif request_type == OTPRequestType.VERIFY:
            otp = payload.get('otp', None)

            if not otp:
                raise BadRequestError('invalid otp')
            
            new_password = payload.get('new_password', None)
            
            if not validations.is_valid_password(new_password):
                raise BadRequestError('invalid password')

            access_util.verify_otp(
                email=email,
                otp=otp
            )

            profile_service.set_password(user, new_password)

            response = {
                "password_updated": True
            }
        else:
            raise BadRequestError('invalid request type')
            
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
    "Delete a user"
    permission_classes = (IsAuthenticated,)

    def delete(self, request):

        user = request.user
        if not user:
            raise BadRequestError('invalid user')

        profile_service.delete_user(user)

        response = {
            "user_deleted": True
        }

        return self.get_success_response(json_response=response)


class GetProfileView(APIView, APIResponse):
    """Get user profile"""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        
        response = profile_service.get_user_profile(request.user)
        
        return self.get_success_response(json_response=response)


class UpdateProfileView(APIView, APIResponse):
    """Update the user info"""
    permission_classes = (IsAuthenticated,)

    def put(self, request):

        payload: dict = request.data

        user = request.user

        first_name = payload.get('first_name', None)
        if not first_name:
            raise BadRequestError(message='invalid first_name')
        
        last_name = payload.get('last_name', None)
        if not last_name:
            raise BadRequestError(message='invalid last_name')

        # update user
        profile_service.update_user(email=user.email, first_name=first_name, last_name=last_name)

        response = {
            "profile_udpated": True
        }

        return self.get_success_response(json_response=response)
