from datetime import datetime
from datetime import timedelta

from oauth2_provider.models import AccessToken
from oauth2_provider.models import Application
from oauth2_provider.models import RefreshToken
from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token

from access.models import User
from main.mixins import errors
from main.mixins.exceptions import UnexpectedRequestError
from main.settings.env import AUTH_APPLICATION_NAME


def create_new_auth_tokens(user: User) -> dict[str, str]:
    """Create access and refresh token"""

    auth_app = Application.objects.filter(name=AUTH_APPLICATION_NAME).last()
    if not auth_app:
        raise UnexpectedRequestError(
            message=f'{errors.NOT_FOUND_ERROR}: auth application',
        )

    expires_at = datetime.now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    access_token = AccessToken.objects.create(
        user=user,
        application=auth_app,
        scope='read write',
        token=generate_token(),
        expires=expires_at,
    )
    refresh_token = RefreshToken.objects.create(
        user=user,
        application=auth_app,
        token=generate_token(),
        access_token=access_token,
    )

    return {
        'access_token': access_token.token,
        'refresh_token': refresh_token.token,
    }
