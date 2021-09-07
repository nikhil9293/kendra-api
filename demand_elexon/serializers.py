from rest_framework import serializers
from demand_elexon.models import Demand

class DemandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demand
        fields = ('Date', 'Time', 'Demand')