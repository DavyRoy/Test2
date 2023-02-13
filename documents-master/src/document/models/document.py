import uuid
from django.db import models
from django.utils import timezone


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_document = models.CharField(max_length=255)
    type = models.ForeignKey('document.TypeDocument', on_delete=models.CASCADE)
    preview_image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    is_archive = models.BooleanField(default=False)
    created_by = models.CharField(max_length=55)
    updated_by = models.CharField(max_length=55, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.name_document}'

    class Meta:
        ordering = ["-created_at"]
