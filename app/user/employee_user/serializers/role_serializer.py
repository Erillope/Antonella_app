from src.user.employee_user.services.dto import RoleDto
from rest_framework import serializers

class RoleSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=250, allow_blank=True, required=False)