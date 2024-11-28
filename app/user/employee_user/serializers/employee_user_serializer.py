from src.user.account import AccountStatus
from src.user.employee_user.services.dto import EmployeeUserDto
from app.user.account.serializers import UserSerializer
from rest_framework import serializers

class EmployeeUserSerializer(UserSerializer):
    roles = serializers.ListField(
        child=serializers.CharField(max_length=25),
        allow_empty=False)
        