from rest_framework import serializers

class RenameRoleSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=250)
    new_role = serializers.CharField(max_length=250)