from rest_framework import serializers
from posts import models

class FeedsSerializers(serializers.ModelSerializer):
  class Meta:
    model = models.Feeds
    fields = '__all__'
    
class StoriesSerializers(serializers.ModelSerializer):
  class Meta:
    model = models.Stories
    fields = '__all__'

class CommentsSerializers(serializers.ModelSerializer):
  class Meta:
    model = models.Comments
    fields = '__all__'

class InteractionsSerializers(serializers.ModelSerializer):
  class Meta:
    model = models.Interactions
    fields = '__all__'