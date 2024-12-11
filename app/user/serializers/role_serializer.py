from rest_framework import serializers

class RoleSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=250)
    created_date = serializers.DateField()

class GetListRoleSerializer(serializers.Serializer):
    roles = serializers.ListField(child=RoleSerializer())