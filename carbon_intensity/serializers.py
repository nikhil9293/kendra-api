from rest_framework import serializers
from carbon_intensity.models import Intensity

class IntensitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intensity
        fields = ('From', 'To', 'Intensity')
     