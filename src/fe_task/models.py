from django.contrib.auth import get_user_model
from django.db import models
from fe_core.models import UUIDModel, Entity

User = get_user_model()


class Task(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
