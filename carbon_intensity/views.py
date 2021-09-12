from carbon_intensity.serializers import IntensitySerializer
from django.shortcuts import render
from carbon_intensity.models import Intensity
# from carbon_intensity.serializers import Intensity
from rest_framework import viewsets


class IntensityViewSet(viewsets.ModelViewSet):
    queryset = Intensity.objects.all()
    serializer_class = IntensitySerializer
    
    def dispatch(self, *args, **kwargs):
        os.system('python3 /code/carbon_intensity/carbon.py')
        os.system('python3 manage.py migrate carbon_intensity zero')
        os.system('python3 manage.py migrate carbon_intensity')
        os.system('python3 manage.py loaddata carbon_intensity')
        return super(IntensityViewSet, self).dispatch(*args, **kwargs)

    

# Create your views here.
