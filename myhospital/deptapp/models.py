# PredictionApp/models.py

from django.db import models

class VisitReason(models.Model):
    reason_text = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    age=models.IntegerField(default=30)
    gender=models.CharField(max_length=10,default='other')

    def __str__(self):
        return self.reason_text
