from rest_framework import serializers

class DisableSerializer(serializers.Serializer):
    id = serializers.UUIDField()