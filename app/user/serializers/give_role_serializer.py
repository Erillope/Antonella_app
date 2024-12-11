from rest_framework import serializers
     
class GiveRoleSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    roles = serializers.ListField(
        child=serializers.CharField(max_length=25),
        allow_empty=False)