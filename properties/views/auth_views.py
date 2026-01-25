from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from properties.serializers.user_slzer import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny)
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny)