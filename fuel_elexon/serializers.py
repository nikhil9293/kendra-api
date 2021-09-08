from rest_framework_json_api import serializers
from .models import fuel

class fuelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = fuel
        fields = ('Date', 'GasTurbine', 'Coal', 'Nuclear', 'Hydro', 'Other')