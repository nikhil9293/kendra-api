from django.db import models

class Transmit(models.Model):
    Date = models.CharField(max_length=200)
    Volume = models.CharField(max_length=200)
    

# Create your models here.
