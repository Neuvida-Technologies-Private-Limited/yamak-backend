import uuid
from django.db import models
from djutil.models import TimeStampedModel
from access.models import User
from access.constants import UserTypes

class Workspace(TimeStampedModel):
    """
    Workspace created by user.
    """

    name = models.CharField(max_length=60, default=None, blank=False)
    workspace_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        blank=False
    )
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='workspace_user_mapping',
        blank=False
    )

class Experiment(TimeStampedModel):
    """
    Experiment created by user.
    """

    name = models.CharField(max_length=60, default=None, blank=False)
    experiment_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        blank=False
    )
    workspace = models.ForeignKey(
        to=Workspace,
        on_delete=models.PROTECT,
        related_name='experiment_workspace_mapping',
        blank=False
    )













