from rest_framework_json_api import serializers
from .models import solar

class solarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = solar
        fields = ('EnergyGenerated', 'Date', 'Time')