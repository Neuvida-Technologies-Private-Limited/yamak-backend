from main.mixins.constants import AppEnvironment
from main.mixins.constants import AppEnvironments
from main.settings.env import APP_ENV

if not APP_ENV or APP_ENV not in AppEnvironments:
    raise Exception(f'APP_ENV = {APP_ENV} is not implemented')

IS_PRODUCTION = APP_ENV == AppEnvironment.PRODUCTION

# initialize singleton resources like: firebase, sentry ...
