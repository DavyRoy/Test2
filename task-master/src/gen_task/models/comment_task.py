import uuid

from django.db import models
from django.utils import timezone


class CommentTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=3000)
    task = models.ForeignKey('gen_task.Task', on_delete=models.CASCADE, related_name='task_comments')
    is_system_comment = models.BooleanField(default=False)
    updated_by = models.CharField(max_length=55, blank=True, null=True)
    created_by = models.CharField(max_length=55)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.created_by} {self.task.name} {self.text}'

    class Meta:
        ordering = ["created_at"]
