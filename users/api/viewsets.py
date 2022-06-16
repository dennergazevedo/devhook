from rest_framework import viewsets
from users.api import serializers
from users import models

class UsersViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UsersSerializer
  queryset = models.Users.objects.all()