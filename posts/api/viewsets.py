from rest_framework import viewsets
from posts.api import serializers
from posts import models

class FeedsViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.FeedsSerializers
  queryset = models.Feeds.objects.all()

class StoriesViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.StoriesSerializers
  queryset = models.Stories.objects.all()

class CommentsViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.CommentsSerializers
  queryset = models.Stories.objects.all()
  
class InteractionsViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.InteractionsSerializers
  queryset = models.Interactions.objects.all()