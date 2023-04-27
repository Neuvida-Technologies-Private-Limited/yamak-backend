from access.models import Country
from access.services import auth_service
from access.services import profile_service
from main import IS_PRODUCTION
from main.mixins.exceptions import BadRequestError
from main.settings import env


def generate_otp(phone: str, dialing_code: str):
    """Generate and send OTP to phone"""

    otp = auth_service.create_otp(phone=phone)
    if IS_PRODUCTION or not env.OTP_DISABLED:
        # todo: send OTP
        pass


def verify_otp(phone: str, otp: str, country: Country) -> dict[str, str]:
    """Verify OTP, create an access and refresh token"""

    if IS_PRODUCTION or not env.OTP_DISABLED:
        otp_entry = auth_service.get_otp(phone=phone, otp=otp)
        if not otp_entry:
            raise BadRequestError('incorrect otp')

    user = profile_service.get_user(phone=phone)
    if not user:
        user = profile_service.create_user(country=country, phone=phone)

    profile_service.update_last_login(user=user)
    tokens = auth_service.create_auth_tokens(user=user)
    if otp_entry:
        # expire OTP if exists
        auth_service.expire_otp(otp_entry=otp_entry)

    return tokens
