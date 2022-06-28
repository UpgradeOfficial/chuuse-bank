from dataclasses import fields
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['user_type'] = user.user_type
        # ...

        return token

class UserRegistrationSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(max_length=10, source="username")
    account_amount = serializers.CharField()
    class Meta:
        model = User
        fields = ['']
        # exclude = ['groups','user_permissions', 'auth_povider'] + User.get_hidden_fields()
        # read_only_fields = ('is_active', 'is_staff')
        # extra_kwargs = {
        #     'user_type': {'write_only': True},
            
        # }