from django.db import models

class freq(models.Model):
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)

# Create your models here.
