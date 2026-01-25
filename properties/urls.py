from django.urls import path
from .views import predict_property, RegisterView, MyTokenObtainPairView, PredictionHistoryList
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('predict/', predict_property, name='predict'),
    path("auth/register", RegisterView.as_view(), name="register"),
    path("auth/login", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("history/", PredictionHistoryList.as_view(), name="history"),
    
]