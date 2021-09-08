from .serializers import windOffSerializer
from django.shortcuts import render
from .models import wind_off
from rest_framework import viewsets


class WindoffViewSet(viewsets.ModelViewSet):
    queryset = wind_off.objects.all()
    serializer_class = windOffSerializer

# Create your views here.
