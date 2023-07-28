from django.db import models
from djutil.models import TimeStampedModel
import uuid
from access.models import User
from .constants import StatusTypes

class Ticket(TimeStampedModel):
    """
    Ticket created by user911.
    """
    status = models.CharField(
        choices=StatusTypes.choices,
        max_length=18,
        default=StatusTypes.CREATED,
        blank=False,
        null=False,
    )
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    report = models.CharField(max_length=100, default=None, blank=False)
    location = models.CharField(max_length=100, default=None, blank=False)
    # Add image in the tickets too
    user_image = models.ImageField(upload_to='images') 
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True, related_name='Ticket creator+')
    disptach_center = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, default=None)
