from django.db import models

class Intensity(models.Model):
    From = models.CharField(max_length=200)
    To = models.CharField(max_length=200)
    Intensity = models.IntegerField()

