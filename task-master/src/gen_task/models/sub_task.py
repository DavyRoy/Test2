from django.db import models

from .basic_model import BasicModel


class SubTask(BasicModel):
    task = models.ForeignKey('gen_task.Task', on_delete=models.CASCADE, related_name='sub_tasks')
    is_completed = models.BooleanField(default=False)
    executor = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["created_at"]
