# core/services/prediction_service.py
from django.contrib.auth.models import User
from core.models.prediction import PredictionHistory
from .ai_service import HuggingFaceClient

class PredictionUseCase:
    def __init__(self):
        self.ai_client = HuggingFaceClient()

    def make_prediction_and_save(self, user: User, data: dict) -> dict:
        """
        Lógica principal:
        1. Valida (implícito o explícito)
        2. Obtiene predicción externa
        3. Guarda historial
        4. Retorna resultado limpio
        """
        
        # 1. Llamar a la IA
        price = self.ai_client.get_prediction(data)
        
        # 2. Guardar en Base de Datos (Historial)
        # Observa cómo creamos el registro aquí, no en la vista
        history = PredictionHistory.objects.create(
            user=user,
            sq_meters=data['sq_meters'],
            rooms=data['rooms'],
            bathrooms=data['bathrooms'],
            garage=data['garage'],
            year_built=data['year_built'],
            location=data['location'],
            estimated_price=price
        )
        
        # 3. Retornar lo que necesita el Frontend
        return {
            "estimated_price": price,
            "currency": "USD",
            "prediction_id": history.id,
            "date": history.created_at
        }