from uuid import uuid4

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager

User = get_user_model()


class Accomplishment(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.TextField()
    challenge = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    reward = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    notes = models.TextField(blank=True)

    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}'s pat {self.uuid}"
