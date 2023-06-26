from django.db import models

class OTPRequestType:

    GENERATE = 'GENERATE'
    VERIFY = 'VERIFY'

class UserTypes(models.TextChoices):

    ADMIN = 'ADMIN'
    USER = 'USER'

class Permissions(models.TextChoices):
    ALL = 'ALL'
