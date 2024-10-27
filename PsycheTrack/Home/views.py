from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserCreateSerializer, LoginSerializer
from django.contrib.auth import login


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

        # Custom error messages
        errors = {}
        if 'username' in serializer.errors:
            errors['username'] = "Username is already taken. Please choose a different one."
        if 'email' in serializer.errors:
            errors['email'] = "This email address is already registered."
        if 'password' in serializer.errors:
            errors['password'] = "Password did not meet the required criteria."

        # Add a generic error message if specific ones are not defined
        if not errors:
            errors['general'] = "There was an issue with the registration. Please check your inputs."

        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


# Landing page view
def landing(request):
    return render(request, 'LandingPage.html')


# Signup view with form
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Dashboard")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)

        # Custom error messages for login
        errors = {}
        if 'email' in serializer.errors:
            errors['email'] = "No account found with this email address."
        if 'password' in serializer.errors:
            errors['password'] = "Incorrect password. Please try again."

        # General error message if specific ones are not set
        if not errors:
            errors['general'] = "Login failed. Please check your email and password."

        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
