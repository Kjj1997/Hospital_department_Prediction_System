from rest_framework import serializers
from .models import VisitReason

class VisitReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitReason
        fields = '__all__'
