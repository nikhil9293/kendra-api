from fuel_elexon.serializers import fuelSerializer
from django.shortcuts import render
from .models import fuel
from rest_framework import viewsets


class fuelViewSet(viewsets.ModelViewSet):
    queryset = fuel.objects.all()
    serializer_class = fuelSerializer

# Create your views here.
