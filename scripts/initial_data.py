from oauth2_provider.models import Application

from access.models import Country
from main.settings.env import AUTH_APPLICATION_NAME


def exec_initial_data():
    '''Add initial data for development'''
    
    print('initial country: India (IN. +91)')
    __add_update_country('India', 'IN', '91')

    print('initial auth app')
    __add_auth_application()


def __add_update_country(name, country_code, dialing_code):

    country, created = Country.objects.update_or_create(
        name=name.strip(),
        defaults={
            'country_code': country_code.strip().upper(),
            'dialing_code': dialing_code,
        },
    )
    return country


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
