from rest_framework_json_api import serializers
from .models import Demand

class DemandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demand
        fields = ('Date', 'Time', 'Demand')