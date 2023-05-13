import base64
import random
from datetime import datetime
from datetime import timedelta

from oauth2_provider.models import Application
from oauth2_provider.models import RefreshToken
from pyotp import TOTP

from access.models import OneTimePassword
from access.models import User
from access.utils import auth_util
from main.mixins import errors
from main.mixins.exceptions import UnAuthorizedError
from main.mixins.exceptions import UnexpectedRequestError
from main.settings import env


def create_otp(email: str) -> str:
    """
    Using a package pyotp to generate one time password
    The password will be saved to OneTimePassword
    """

    random_key = random.shuffle(list(email))
    timestamp = datetime.now().timestamp()
    otp_secret = f'{random_key}-{timestamp}-{env.OTP_SECRET}'
    otp_secret = base64.b32encode(
        bytearray(otp_secret, 'ascii'),
    ).decode('utf-8')

    totp = TOTP(s=otp_secret)
    otp = totp.now()
    expires_at = datetime.now() + timedelta(minutes=env.OTP_EXPIRY_IN_MIN)

    OneTimePassword.objects.update_or_create(
        email=email,
        password=otp,
        defaults={
            'expires_at': expires_at,
        },
    )

    return otp


def get_otp(email: str, otp: str) -> OneTimePassword:
    """Get OTP for a phone if not expired"""

    otp_qs = OneTimePassword.objects.filter(
        email=email,
        password=otp,
        expires_at__gte=datetime.now(),
    )
    if not otp_qs.exists():
        return None

    return otp_qs.last()


def expire_otp(otp_entry: OneTimePassword):

    otp_entry.expires_at = otp_entry.expires_at - timedelta(days=1)
    otp_entry.save()


def create_auth_tokens(user: User) -> dict[str, str]:
    """Create access and refresh token"""

    auth_app = Application.objects.filter(
        name=env.AUTH_APPLICATION_NAME,
    ).last()
    if not auth_app:
        raise UnexpectedRequestError(
            message=f'{errors.NOT_FOUND_ERROR}: auth application',
        )

    tokens = auth_util.create_new_auth_tokens(user=user)
    return tokens


def refresh_new_token(refresh_token: str, access_token: str) -> dict[str, str]:

    r_token: RefreshToken = RefreshToken.objects.filter(
        token=refresh_token,
        access_token__token=access_token,
        revoked=None,
    ).last()
    if not r_token:
        raise UnAuthorizedError(errors.UNAUTHORIZED_ERROR)

    r_token.revoke()
    tokens = auth_util.create_new_auth_tokens(user=r_token.user)
    return tokens


def revoke_token(user_id: int, access_token: str):
    """Also used for logout"""

    r_token: RefreshToken = RefreshToken.objects.filter(
        user_id=user_id,
        access_token__token=access_token,
        revoked=None,
    ).last()
    if r_token:
        r_token.revoke()

