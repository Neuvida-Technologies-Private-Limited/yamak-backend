from datetime import datetime
from rest_framework.exceptions import ValidationError
from access.models import Country
from access.models import User
from access.serializers import UserSerializer, UserSerializerEmail, UserSerializerEmailWithoutProfile


def get_country(country_code: str) -> Country:

    # querying as last because don't need to raise error on get
    return Country.objects.filter(country_code=country_code)

def get_country_object(country_code: str) -> Country:

    # querying as last because don't need to raise error on get
    return Country.objects.filter(country_code=country_code).last()

def get_user(phone: str) -> User:
    """Get an auth user by phone"""

    user_qs = User.objects.filter(phone=phone)
    if not user_qs.exists():
        return None

    return user_qs.last()


def get_user_email(email: str) -> User:
    """Get an auth user by email"""

    user_qs = User.objects.filter(email=email)

    if not user_qs.exists():
        return None

    return user_qs.last()


def set_password(user: User, password: str):
    """Set password of the user"""
    user.set_password(password)
    user.save()


def create_user(country: Country, phone: str, first_name: str, last_name: str) -> User:
    """Create a new auth user"""

    user = {
        'phone': phone,
        'country': country.id,
        'first_name': first_name,
        'last_name': last_name
    }
    ser = UserSerializer(data=user)
    if not ser.is_valid():
        raise ValidationError(ser.errors)

    return ser.save()


def create_user_email(email: str, is_sso, is_validated, first_name: str = None, last_name: str = None ) -> User:
    """Create a new auth user with email"""

    user = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'is_sso': is_sso,
        'is_validated': is_validated
    }
    ser = UserSerializerEmail(data=user)

    if not ser.is_valid():
        raise ValidationError(ser.errors)

    return ser.save()

def create_user_email_without_profile(email: str, is_sso, is_validated) -> User:
    """Create a new auth user with email"""

    user = {
        'email': email,
        'is_sso': is_sso,
        'is_validated': is_validated
    }
    ser = UserSerializerEmailWithoutProfile(data=user)

    if not ser.is_valid():
        raise ValidationError(ser.errors)

    return ser.save()


def update_last_login(user: User):
    user.last_login = datetime.today()
    user.save()