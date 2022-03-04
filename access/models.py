from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from djutil.models import TimeStampedModel

from access.managers import UserManager


class Country(TimeStampedModel):
    """Which country we are operating in?"""

    name = models.CharField(max_length=32, unique=True)
    country_code = models.CharField(max_length=4, unique=True)
    # store dialing code as 91 and not +91
    dialing_code = models.CharField(max_length=4, unique=True)


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    All the users who will access the system.
    Auth level custom user.
    An unique user is defined by an unique phone.
    Needs a custom User Manager.
    It will be used for system roles and access.
    """

    phone = models.CharField(max_length=10, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    country = models.ForeignKey(
        to=Country,
        on_delete=models.PROTECT,
        related_name='users',
    )

    objects = UserManager()

    USERNAME_FIELD = 'phone'


class OneTimePassword(TimeStampedModel):
    """
    OTP saved for a phone for authentication.
    """

    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    expires_at = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['phone', 'password'],
                name='unique_otp',
            ),
        ]
