from rest_framework import serializers
from properties.models.prediction import PredictionHistory
class PredictionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionHistory
        fields = "__all__"