from .serializers import WindOnSerializer
from django.shortcuts import render
from .models import wind_on
from rest_framework import viewsets


class WindonViewSet(viewsets.ModelViewSet):
    queryset = wind_on.objects.all()
    serializer_class = WindOnSerializer


