# core/views/api_views.py

from django.http import JsonResponse
from properties.services.prediction_service import PredictionUseCase
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from properties.serializers import PredictionHistorySerializer
from properties.models.prediction import PredictionHistory

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def predict_property(request):
    """
    Endpoint: POST /api/predict/
    """
    try:
        # 1. Parsear Request
        data = request.data
        user = request.user
        # 2. Instanciar Servicio
        service = PredictionUseCase()
        
        # 3. Ejecutar Lógica
        result = service.make_prediction_and_save(user, data)
        
        # 4. Responder
        return JsonResponse(result, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

class PredictionHistoryList(generics.ListAPIView):
    serializer_class = PredictionHistorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return PredictionHistory.objects.filter(user=self.request.user).order_by("-created_at")