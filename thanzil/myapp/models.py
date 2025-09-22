from django.db import models

class Car(models.Model):
    car_id = models.IntegerField()
    model_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField()

    def str(self):
        return f"{self.manufacturer} {self.model_name} ({self.year})"
