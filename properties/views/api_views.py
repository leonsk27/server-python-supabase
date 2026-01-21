# core/views/api_views.py
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from core.services.prediction_service import PredictionUseCase

@csrf_exempt  # Usar Token Authentication en producción real
# @login_required # Descomentar si usas autenticación de sesión
def predict_property(request):
    """
    Endpoint: POST /api/predict/
    """
    try:
        # 1. Parsear Request
        data = json.loads(request.body)
        
        # Simulamos usuario si no hay auth configurada aún (para pruebas)
        user = request.user if request.user.is_authenticated else None
        if not user:
            return JsonResponse({'error': 'Usuario no autenticado'}, status=401)

        # 2. Instanciar Servicio
        service = PredictionUseCase()
        
        # 3. Ejecutar Lógica
        result = service.make_prediction_and_save(user, data)
        
        # 4. Responder
        return JsonResponse(result, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)