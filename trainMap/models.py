import json
from datetime import datetime

from django.db import models
from django.http import JsonResponse


class TrainData(models.Model):
    train_id = models.CharField(max_length=100)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def to_json(cls):
        # Sérialise les instances réelles, pas les descripteurs de classe.
        data = [
            {
                "id": obj.train_id,
                "lattitude": obj.lattitude,
                "longitude": obj.longitude,
                "speed": obj.speed,
                "timestamp": obj.timestamp.isoformat(),
            }
            for obj in cls.objects.all()
        ]
        return JsonResponse(data, safe=False, json_dumps_params={"indent": 4})

    def __str__(self):
        return f"TrainData(id={self.train_id}, lat={self.lattitude}, lon={self.longitude}, speed={self.speed})"
