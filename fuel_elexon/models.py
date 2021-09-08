from django.db import models

class fuel(models.Model):
    Date = models.CharField(max_length=200)
    GasTurbine = models.CharField(max_length=200)
    Coal = models.CharField(max_length=200)
    Nuclear = models.CharField(max_length=200)
    Hydro = models.CharField(max_length=200)
    Other = models.CharField(max_length=200)

# Create your models here.
