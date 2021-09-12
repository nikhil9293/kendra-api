from demand_elexon.serializers import DemandSerializer
from django.shortcuts import render
from demand_elexon.models import Demand
# from demand_elexon.serializers import Demand
from rest_framework import viewsets

class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
    def dispatch(self, *args, **kwargs):
        os.system('python3 /code/freq_elexon/freq.py')
        os.system('python3 manage.py migrate freq_elexon zero')
        os.system('python3 manage.py migrate freq_elexon')
        os.system('python3 manage.py loaddata freq_elexon')
        return super(DemandViewSet, self).dispatch(*args, **kwargs)
    

# Create your views here.
