from oauth2_provider.models import Application
from main.settings.env import AUTH_APPLICATION_NAME
from access.models import UserType
from access.constants import UserTypes

def exec_initial_data():
    '''Add initial data for development'''

    print('initial auth app')
    __add_auth_application()
    print('types of users')
    __add_user_types()

def __add_auth_application():

    auth_app = Application.objects.filter(name=AUTH_APPLICATION_NAME).last()
    if not auth_app:
        auth_app, created = Application.objects.update_or_create(
            name=AUTH_APPLICATION_NAME,
            defaults={
                'client_type': Application.CLIENT_CONFIDENTIAL,
                'authorization_grant_type': Application.GRANT_CLIENT_CREDENTIALS,
            },
        )
    return auth_app

def __add_user_types():

    for user_type in UserTypes:
        UserType.objects.update_or_create(user_type=user_type)
     
    return