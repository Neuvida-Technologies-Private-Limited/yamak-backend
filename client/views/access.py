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


class OTPView(APIView, APIResponse):
    """Generate and verifying OTP for consumer login"""

    def post(self, request):

        payload: dict = request.data
        phone = payload.get('phone', None)
        if not validations.is_valid_phone(phone):
            raise BadRequestError(message='invalid phone')

        country = profile_service.get_country(
            country_code=payload.get('country_code', None),
        )
        if not country:
            raise BadRequestError(message='invalid country')

        request_type = payload.get('request_type', None)
        if request_type == OTPRequestType.GENERATE:
            access_util.generate_otp(
                phone=phone,
                dialing_code=country.dialing_code,
            )
            response = {
                'country_code': country.country_code,
                'phone': phone,
                'request_type': request_type,
            }
        elif request_type == OTPRequestType.VERIFY:

            otp = payload.get('otp', None)
            response = access_util.verify_otp(
                phone=phone,
                otp=otp,
                country=country,
            )
        else:
            raise BadRequestError('invalid otp request type')

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
