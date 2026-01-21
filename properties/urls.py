from django.urls import path
from .views import predict_property

urlpatterns = [
    path('predict/', predict_property, name='predict'),
]