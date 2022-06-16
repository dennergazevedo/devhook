from django.db import models
from uuid import uuid4

class Users(models.Model):
  userId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  email = models.CharField(unique=True, max_length=255)
  password = models.CharField(max_length=20)
  firstName = models.CharField(max_length=255)
  lastName = models.CharField(max_length=255)
  photo = models.FileField(upload_to='uploads/profile')
  about = models.TextField(blank=True)
  token = models.TextField(blank=True, null=True)
  create_at = models.DateField(auto_now_add=True)
  
  @property
  def password(self):
    return self.password

  @password.setter
  def password(self, value):
    self.password = value