from datetime import datetime

from rest_framework.exceptions import ValidationError

from access.models import User, UserType
from access.serializers import UserSerializer
from access.constants import UserTypes

def get_user(email: str) -> User:
    """Get an auth user"""

    user_qs = User.objects.filter(email=email)
    if not user_qs.exists():
        return None

    return user_qs.last()

def delete_user(user: User) -> None:
    "Delete an user"
    user.delete()
    return
        
def update_user(email: str, first_name: str, last_name: str) -> User:
    """Update an auth user"""

    User.objects.filter(email=email).update(first_name=first_name, last_name=last_name)
    return

def get_user_profile(user: User):

    # user_type id
    user_type_id = user.__dict__['user_type_id']

    # User Type object
    user_type = UserType.objects.filter(id=user_type_id).last()

    # collect profile details
    profile_details = {
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'user_type': user_type.__dict__['user_type']
    }

    return profile_details

def get_dispatch_centers():

    # Extract the user id
    user_id = get_user_type_id(UserTypes.DISPATCH_CENTER)

    # Get disptach centers list
    dispatch_centers = list(User.objects.filter(user_type=user_id).values('first_name', 'last_name', 'email'))

    return dispatch_centers

def create_user(email: str, password: str, first_name: str, last_name: str, user_type) -> User:
    """Create a new auth user"""

    user = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'user_type': get_user_type_id(user_type)
    }

    ser = UserSerializer(data=user)

    if not ser.is_valid():
        raise ValidationError(ser.errors)

    user = ser.save()
    
    set_password(user, password)

    return user


def set_password(user: User, password: str):
    """Set password of the user"""
    user.set_password(password)
    user.save()
    return

def update_last_login(user: User):
    user.last_login = datetime.today()
    user.save()

def get_user_type():
    """Check if user_type is correct"""

    user_type = list(UserType.objects.all().values('user_type'))

    return user_type

def get_user_type_by_id(user_type_id: str):
    """Check if user_type is correct"""

    user_type = list(UserType.objects.filter(id=user_type_id).values('user_type'))

    return user_type[0]

def check_user_type(user_type: str):
    """Check if user_type is correct"""
    user_types = get_user_type()

    for value in user_types:
        if value.get('user_type') == user_type:
            return True

    return False

def get_user_type_id(user_type: str):
    """Check if user_type is correct"""

    user_type = UserType.objects.filter(user_type=user_type).last()

    # convert to dict
    user_type = user_type.__dict__

    return user_type['id']
