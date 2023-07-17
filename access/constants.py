from django.db import models

class OTPRequestType:

    GENERATE = 'GENERATE'
    VERIFY = 'VERIFY'

class UserTypes(models.TextChoices):

    USER911 = 'USER911'
    FIREFIGHTER = 'FIREFIGHTER'
    DISPATCH_CENTER = 'DISPATCH_CENTER'

class Permissions(models.TextChoices):
    ALL = 'ALL'
