from django.shortcuts import get_object_or_404
from oauth2_provider.models import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# from access.constants import OTPRequestType
# from access.services import auth_service
# from access.services import profile_service
from client.utils import access_util
from main.mixins import validations
from main.mixins.exceptions import BadRequestError
from main.mixins.exceptions import UnAuthorizedError
from main.mixins.views import APIResponse
