import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
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

# sentry setup
sentry_sdk.init(
    environment=env.APP_ENV,
    dsn="https://4eb5085ecee5497f9755f8e98cae9af4@o1055993.ingest.sentry.io/4505169887166464",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)