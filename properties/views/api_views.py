# core/views/api_views.py
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from properties.services.prediction_service import PredictionUseCase
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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