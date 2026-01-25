from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from properties.serializers.user_slzer import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import logging

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    # 3. Sobrescribir el método create para inyectar los logs
    def create(self, request, *args, **kwargs):
        username = request.data.get('username', 'Desconocido')
        
        try:
            logger.info(f"📩 Intento de registro recibido para: {username}")
            
            # Ejecuta la lógica original de creación
            response = super().create(request, *args, **kwargs)
            
            logger.info(f"✅ Usuario {username} creado exitosamente. ID: {response.data.get('id')}")
            return response
            
        except Exception as e:
            logger.error(f"❌ Error crítico registrando a {username}: {str(e)}")
            raise e

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny)