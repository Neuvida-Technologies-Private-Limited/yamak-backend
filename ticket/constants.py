from django.db import models

class StatusTypes(models.TextChoices):

    CREATED = 'CREATED'
    ASSIGNED = 'ASSIGNED'
    RESOLVED = 'RESOLVED'
    FALSE_ALARM = 'FALSE_ALARM'
