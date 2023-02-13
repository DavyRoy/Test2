import uuid
from django.db import models
from django.utils import timezone


class TypeDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    activity = models.BooleanField(default=False)
    created_by = models.CharField(max_length=55)
    updated_by = models.CharField(max_length=55, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ["-created_at"]
