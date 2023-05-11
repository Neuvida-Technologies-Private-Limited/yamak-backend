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

    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=254, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=60, default=None, blank=True)
    last_name = models.CharField(max_length=60, default=None, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_sso = models.BooleanField(default=False)
    is_validated = models.BooleanField(default=False)
    country = models.ForeignKey(
        to=Country,
        on_delete=models.PROTECT,
        related_name='users',
        null=True,
        blank=True
    )

    class Meta:

        constraints = [
            models.CheckConstraint(
                check=models.Q(phone__isnull=False) | models.Q(email__isnull=False),
                name='not_both_null'
            )
        ]

    objects = UserManager()

    USERNAME_FIELD = 'id'

    def __str__(self):
        return self.email or self.phone


class OneTimePassword(TimeStampedModel):
    """
    OTP saved for a phone/email for authentication.
    """
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    password = models.CharField(max_length=8)
    expires_at = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['phone', 'password'],
                name='unique_otp',
            ),
            models.UniqueConstraint(
                fields=['email', 'password'],
                name='unique_email',
            ),
            models.CheckConstraint(
                check=models.Q(phone__isnull=False) | models.Q(email__isnull=False),
                name='email_phone_not_null'
            )
        ]