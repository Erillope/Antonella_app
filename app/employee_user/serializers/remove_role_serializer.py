from rest_framework import serializers
     
class RemoveRoleSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=250, allow_blank=True, required=False)