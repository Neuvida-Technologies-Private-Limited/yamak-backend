from . import env

# other supported third party apps
OTHER_TP_APPS = [
    # oauth support
    'oauth2_provider',

    # other extensions (e.g. shell_plus, generating model visualizations)
    'django_extensions',

    'django_filters',
]

# projects apps to be added to installed apps
PROJECTS_APPS = [
    'access',
    'user',
    'workspace'
]

# setup rest framework configs
REST_FRAMEWORK = {

    # for AUTH authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),

    # for filter feature
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),

    # for pagination size
    'PAGE_SIZE': 15,
}

OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# security related
if env.APP_ENV != 'dev':
    # make sure browser sends csrf cookies on HTTPS
    CSRF_COOKIE_SECURE = True
    # trust that the request came via HTTPS
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # make sure browser sends session cookies on HTTPS
    SESSION_COOKIE_SECURE = True
    # redirect all non-HTTPS to HTTPS
    SECURE_SSL_REDIRECT = True
