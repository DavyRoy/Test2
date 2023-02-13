import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    kpi = models.DecimalField(decimal_places=5, max_digits=20, blank=True, null=True)
    role = models.ManyToManyField('user_api.Role', related_name='users')
    phone = models.CharField(max_length=20, blank=True, null=True)
    updated_by = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='updated_users')
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='created_users')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ["created_at"]
