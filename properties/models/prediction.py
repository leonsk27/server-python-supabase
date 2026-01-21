# core/models/prediction.py
from django.db import models
from django.contrib.auth.models import User

class PredictionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predictions')
    # Inputs
    sq_meters = models.FloatField()
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    year_built = models.IntegerField()
    location = models.CharField(max_length=100)
    
    # Outputs
    estimated_price = models.FloatField()
    currency = models.CharField(max_length=3, default='USD')
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.location} (${self.estimated_price})"