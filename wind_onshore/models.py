from django.db import models

class wind_on(models.Model):
    windtype = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)
    Period = models.CharField(max_length=200)
    EnergyGenerated = models.CharField(max_length=200)

# Create your models here.
