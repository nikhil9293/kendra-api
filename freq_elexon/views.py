from freq_elexon.serializers import freqSerializer
from django.shortcuts import render
from freq_elexon.models import freq
# from carbon_intensity.serializers import Intensity
from rest_framework import viewsets


class freqViewSet(viewsets.ModelViewSet):
    queryset = freq.objects.all()
    serializer_class = freqSerializer


# Create your views here.
