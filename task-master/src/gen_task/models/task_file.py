from django.db import models

from .basic_model import BasicModel


class TaskFile(BasicModel):
    file_id = models.CharField(max_length=2555)
    task = models.ForeignKey('gen_task.Task', on_delete=models.CASCADE, related_name='task_files')

    class Meta:
        ordering = ["created_at"]
