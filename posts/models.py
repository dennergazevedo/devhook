from django.db import models
from uuid import uuid4

class Feeds(models.Model):
  feedId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  userId = models.ForeignKey("users.Users", on_delete=models.CASCADE)
  file = models.FileField(upload_to='uploads/feeds')
  description = models.CharField(max_length=255)
  create_at = models.DateField(auto_now_add=True)

class Stories(models.Model):
  storieId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  userId = models.ForeignKey("users.Users", on_delete=models.CASCADE)
  file = models.FileField(upload_to='uploads/stories')
  create_at = models.DateField(auto_now_add=True)

class Comments(models.Model):
  commentId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  feedId = models.ForeignKey('Feeds', on_delete=models.CASCADE)
  message = models.CharField(max_length=255)
  create_at = models.DateField(auto_now_add=True)
  
class Interactions(models.Model):
  interactionId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  userId = models.ForeignKey('users.Users', on_delete=models.CASCADE)
  feedId = models.ForeignKey('Feeds', on_delete=models.CASCADE, blank=True)
  storieId = models.ForeignKey('Stories', on_delete=models.CASCADE, blank=True)
  type = models.CharField(max_length=255)
  create_at = models.DateField(auto_now_add=True)