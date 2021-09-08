from django.db import models

class Price(models.Model):
    Date = models.CharField(max_length=200)
    Period = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    
# Create your models here.
