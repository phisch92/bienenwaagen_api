# core/models.py
import uuid
from django.conf import settings
from django.db import models


class Scale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid3, editable=False)
    device_id = models.CharField(max_length=16)
    custom_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.custom_name
