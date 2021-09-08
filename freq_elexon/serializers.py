from rest_framework_json_api import serializers
from .models import freq

class freqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = freq
        fields = ('date', 'time', 'frequency')