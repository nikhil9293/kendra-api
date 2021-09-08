from rest_framework_json_api import serializers
from .models import wind_on

class WindOnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wind_on
        fields = ('windtype', 'Date', 'Period', 'EnergyGenerated')