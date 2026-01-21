# core/services/ai_service.py
import requests
from django.conf import settings

class HuggingFaceClient:
    def __init__(self):
        # Es buena práctica leer esto de settings.py (variables de entorno)
        self.api_url = settings.HF_API_URL 
        self.api_token = settings.HF_API_TOKEN

    def get_prediction(self, data: dict) -> float:
        """
        Envía los datos crudos a la IA y retorna solo el precio.
        Maneja errores de conexión aquí.
        """
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(f"{self.api_url}/predict", json=data, headers=headers, timeout=5)
            response.raise_for_status() # Lanza error si no es 200
            
            result = response.json()
            return result.get('estimated_price', 0.0)
            
        except requests.exceptions.RequestException as e:
            # Aquí podrías loguear el error real
            print(f"❌ Error conectando con AI: {e}")
            raise Exception("El servicio de estimación no está disponible temporalmente.")