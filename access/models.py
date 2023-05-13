from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from djutil.models import TimeStampedModel
from access.managers import UserManager
from access.constants import UserType

class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    All the users who will access the system.
    Auth level custom user.
    An unique user is defined by an unique phone.
    Needs a custom User Manager.
    It will be used for system roles and access.
    """

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True, default=None)
    first_name = models.CharField(max_length=60, default=None, blank=False)
    last_name = models.CharField(max_length=60, default=None, blank=False)
    is_validated = models.BooleanField(default=False)
    user_type =  models.CharField(
        choices=UserType.choices,
        max_length=18,
        default=UserType.ADMIN
    )
    objects = UserManager()

    USERNAME_FIELD = 'id'

    def __str__(self):
        return self.email


class OneTimePassword(TimeStampedModel):
    """
    OTP saved for a phone/email for authentication.
    """
    email = models.EmailField(max_length=254, blank=True)
    password = models.CharField(max_length=8)
    expires_at = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'password'],
                name='unique_email',
            ),
            models.CheckConstraint(
                check=models.Q(email__isnull=False),
                name='email_not_null'
            )
        ]
