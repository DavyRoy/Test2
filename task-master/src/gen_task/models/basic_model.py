import uuid
from django.db import models
from django.utils import timezone


class BasicModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Название')
    updated_by = models.CharField(max_length=55, blank=True, null=True)
    created_by = models.CharField(max_length=55)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
