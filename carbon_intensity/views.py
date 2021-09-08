from carbon_intensity.serializers import IntensitySerializer
from django.shortcuts import render
from carbon_intensity.models import Intensity
# from carbon_intensity.serializers import Intensity
from rest_framework import viewsets

class IntensityViewSet(viewsets.ModelViewSet):
    queryset = Intensity.objects.all()
    serializer_class = IntensitySerializer


# Create your views here.
