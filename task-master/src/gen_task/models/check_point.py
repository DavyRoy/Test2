from django.contrib.postgres.fields import ArrayField
from django.db import models

from .basic_model import BasicModel
from .priority import Priority
from .status import Status


class CheckPoint(BasicModel):
    project = models.CharField(max_length=255)
    stage = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='stages')
    is_stage = models.BooleanField(default=False)
    description = models.CharField(max_length=2555)
    executor = models.CharField(max_length=255)
    observers = ArrayField(models.CharField(max_length=255, blank=True, null=True), null=True, blank=True, size=20, default=list)
    priority = models.IntegerField(choices=Priority.choices)
    status = models.IntegerField(choices=Status.choices)
    started_at = models.DateTimeField()
    planned_ended_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)

    @property
    def tasks(self):
        return self.tasks.all()

    @property
    def stages(self):
        return self.stages.all()

    class Meta:
        ordering = ["created_at"]
