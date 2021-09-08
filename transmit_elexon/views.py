from transmit_elexon.models import Transmit
from .serializers import TransmitSerializer
from django.shortcuts import render
from .models import Transmit
from rest_framework import viewsets


class TransmitViewSet(viewsets.ModelViewSet):
    queryset = Transmit.objects.all()
    serializer_class = TransmitSerializer

# Create your views here.
