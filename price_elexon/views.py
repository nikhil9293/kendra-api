from price_elexon.serializers import PriceSerializer
from django.shortcuts import render
from .models import Price
from rest_framework import viewsets


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

# Create your views here.
