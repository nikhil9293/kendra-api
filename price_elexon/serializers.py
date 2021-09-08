from rest_framework_json_api import serializers
from .models import Price

class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ('Date', 'Period', 'Price')