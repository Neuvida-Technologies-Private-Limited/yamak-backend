from os import environ

APP_ENV = environ.get('APP_ENV')
APP_NAME = environ.get('APP_NAME')
DEBUG = bool(int(environ.get('DEBUG', default='0').strip()))
SECRET_KEY = environ.get('SECRET_KEY')
AUTH_APPLICATION_NAME = environ.get('AUTH_APPLICATION_NAME')

# database
DATABASE_HOST = environ.get('DATABASE_HOST')
DATABASE_PORT = environ.get('DATABASE_PORT')
DATABASE_USER = environ.get('DATABASE_USER')
DATABASE_PASS = environ.get('DATABASE_PASS')
DATABASE_NAME = environ.get('DATABASE_NAME')

OTP_SECRET = environ.get('OTP_SECRET')
OTP_DISABLED = bool(int(environ.get('OTP_DISABLED', default='0').strip()))
OTP_EXPIRY_IN_MIN = int(environ.get('OTP_EXPIRY_IN_MIN'))
