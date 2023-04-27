from datetime import datetime

from rest_framework.exceptions import ValidationError

from access.models import Country
from access.models import User
from access.serializers import UserSerializer


def get_country(country_code: str) -> Country:

    # querying as last because don't need to raise error on get
    return Country.objects.filter(country_code=country_code).last()


def get_user(phone: str) -> User:
    """Get an auth user by phone"""

    user_qs = User.objects.filter(phone=phone)
    if not user_qs.exists():
        return None

    return user_qs.last()


def create_user(country: Country, phone: str) -> User:
    """Create a new auth user"""

    user = {
        'phone': phone,
        'country': country.id,
    }
    ser = UserSerializer(data=user)
    if not ser.is_valid():
        raise ValidationError(ser.errors)

    return ser.save()


def update_last_login(user: User):
    user.last_login = datetime.today()
    user.save()
