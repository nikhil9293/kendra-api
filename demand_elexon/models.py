from django.db import models

class Demand(models.Model):
    Date = models.CharField(max_length=200)
    Time = models.CharField(max_length=200)
    Demand = models.CharField(max_length=200)

# Create your models here.
