from rest_framework_json_api import serializers
from .models import wind_off

class windOffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wind_off
        fields = ('Windtype', 'Date', 'Period', 'EnergyGenerated')