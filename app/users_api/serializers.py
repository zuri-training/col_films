from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'username', 'email', 'school', 'registration_date', 'is_staff', 'is_member', 'verified')