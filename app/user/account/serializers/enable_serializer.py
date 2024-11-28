from rest_framework import serializers

class EnableSerializer(serializers.Serializer):
    id = serializers.UUIDField()