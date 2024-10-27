from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def validate(self, data):
        # Check password match
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        # Check if email is unique
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Email is already in use."})

        return data

    def create(self, validated_data):
        # Remove password2 before creating the user
        validated_data.pop('password2')

        # Create user with username, email, and first/last name
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Change from username to email
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Authenticate using email instead of username
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if user.check_password(data['password']):
            return user
        raise serializers.ValidationError("Invalid credentials")
