from datetime import datetime

from rest_framework.exceptions import ValidationError

from access.models import User
from access.serializers import UserSerializer
from access.constants import UserType

def get_user(email: str) -> User:
    """Get an auth user"""

    user_qs = User.objects.filter(email=email)
    if not user_qs.exists():
        return None

    return user_qs.last()

        
def update_user(email: str, first_name: str, last_name: str) -> User:
    """Get an auth user"""

    user_qs = User.objects.filter(email=email).update(first_name=first_name, last_name=last_name)
    if not user_qs.exists():
        return None

    return user_qs.last()

def create_user(email: str, password: str, first_name: str, last_name: str, user_type) -> User:
    """Create a new auth user"""

    user = {
        'email': email,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'user_type': user_type
    }
    ser = UserSerializer(data=user)
    if not ser.is_valid():
        raise ValidationError(ser.errors)

    return ser.save()


def update_last_login(user: User):
    user.last_login = datetime.today()
    user.save()
