from django.db import models

class OTPRequestType:

    GENERATE = 'GENERATE'
    VERIFY = 'VERIFY'

class UserType(models.TextChoices):

    ADMIN = 'ADMIN'
    USER = 'USER'
