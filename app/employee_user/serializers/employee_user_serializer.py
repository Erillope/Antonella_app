from src.user.account import AccountStatus
from src.user.employee_user.services.dto import EmployeeUserDto
from rest_framework import serializers

class EmployeeUserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    account = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=25)
    roles = serializers.ListField(
        child=serializers.CharField(max_length=25),
        allow_empty=False)
    status = serializers.ChoiceField(choices=[(s.name, s.name) for s in AccountStatus])
    joined_date = serializers.DateField()
    
    @staticmethod
    def generate_serializer(dto: EmployeeUserDto) -> "EmployeeUserSerializer":
        data = {"id": dto.get_id(),
                "account": dto.get_account(),
                "name": dto.get_name(),
                "roles": dto.get_roles(),
                "status": dto.get_status().name,
                "joined_date": dto.get_joined_date().isoformat()
                }
        serializer = EmployeeUserSerializer(data=data)
        serializer.is_valid()
        return serializer
        