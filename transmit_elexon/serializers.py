from rest_framework_json_api import serializers
from .models import Transmit

class TransmitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transmit
        fields = ('Date', 'Volume')