from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email')
        model = User


class MyTokenObtainSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    confirmation_code = serializers.CharField(max_length=20)

    class Meta:
        fields = ('username', 'confirmation_code')
        model = User
