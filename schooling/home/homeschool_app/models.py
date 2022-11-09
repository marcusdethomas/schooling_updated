from django.utils import timezone
from django.db import models
from datetime import date
from email.policy import default
from django.core.exceptions import ValidationError as Error
from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(blank=False, max_length=25)
    description = models.TextField()
    tag = models.CharField(max_length=20)
    file = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField()
