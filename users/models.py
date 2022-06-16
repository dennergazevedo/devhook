from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

class Users(AbstractUser):
  userId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  firstName = models.CharField(max_length=255)
  lastName = models.CharField(max_length=255)
  photo = models.FileField(upload_to='uploads/profile')
  about = models.TextField(blank=True)
  create_at = models.DateField(auto_now_add=True)