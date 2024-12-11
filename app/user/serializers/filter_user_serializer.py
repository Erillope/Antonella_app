from src.common import OrdenDirection
from rest_framework import serializers

class FilterUserSerializer(serializers.Serializer):
    expresion = serializers.CharField(max_length=250, allow_blank=True, required=False)
    order_by = serializers.CharField(max_length=250)
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()
    direction = serializers.ChoiceField(choices=[(o.name, o.name) for o in OrdenDirection])