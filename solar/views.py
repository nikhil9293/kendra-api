from .serializers import solarSerializer
from django.shortcuts import render
from .models import solar
from rest_framework import viewsets


class solarViewSet(viewsets.ModelViewSet):
    queryset = solar.objects.all()
    serializer_class = solarSerializer

