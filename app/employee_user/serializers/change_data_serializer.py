from rest_framework import serializers

class ChangeDataSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    account = serializers.CharField(max_length=250, allow_blank=True, required=False)
    name = serializers.CharField(max_length=25, allow_blank=True, required=False)
    password = serializers.CharField(max_length=250, allow_blank=True, required=False)