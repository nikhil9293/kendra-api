from demand_elexon.serializers import DemandSerializer
from django.shortcuts import render
from demand_elexon.models import Demand
from demand_elexon.serializers import Demand
from rest_framework import viewsets

class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

# Create your views here.
