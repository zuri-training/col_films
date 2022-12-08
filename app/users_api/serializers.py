from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        user_data = validated_data.pop('account')
        user = User.objects.create(**user_data)
        return user

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"