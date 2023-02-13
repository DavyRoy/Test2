import uuid

from django.db import models


class TaskAnalyticData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(blank=True, null=True)
    processing = models.DateTimeField(blank=True, null=True)
    on_pause = models.DateTimeField(blank=True, null=True)
    on_review = models.DateTimeField(blank=True, null=True)
    returned = models.DateTimeField(blank=True, null=True)
    finished = models.DateTimeField(blank=True, null=True)
    agreed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.task.name}'
