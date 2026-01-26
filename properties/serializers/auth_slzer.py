from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # 1. Obtiene los tokens por defecto (access, refresh)
        data = super().validate(attrs)

        # 2. Agregamos datos personalizados del usuario
        # self.user es el usuario autenticado en este momento
        data['username'] = self.user.username
        # El response final será: 
        # { "access": "...", "refresh": "...", "username": "juan", "email": "..." }
        return data