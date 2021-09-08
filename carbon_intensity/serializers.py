from rest_framework_json_api import serializers
from .models import Intensity

class IntensitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intensity
        fields = ('From', 'To', 'Intensity')
     