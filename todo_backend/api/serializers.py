from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Task


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_username(self, username):
        existing = User.objects.filter(username=username).first()
        if existing:
            raise serializers.ValidationError("That username already exists.")
        return username

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and confirm that password.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("You did not enter the same password twice.")
        return data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if data.get('username') and data.get('password'):
            authenticate(username=data.get('username'), password=data.get('password'))
        else:
            raise serializers.ValidationError("Must include username and password.")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = []
