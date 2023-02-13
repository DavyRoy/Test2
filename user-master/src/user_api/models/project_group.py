import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone


class ProjectGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    users = models.ManyToManyField('user_api.User', related_name='project_groups')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='updated_project_groups', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_project_groups')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ["created_at"]
