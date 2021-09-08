from django.db import models

class solar(models.Model):
    EnergyGenerated = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)
    Time = models.CharField(max_length=200)

# Create your models here.
