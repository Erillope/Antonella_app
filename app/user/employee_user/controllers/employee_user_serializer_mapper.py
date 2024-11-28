from src.user.employee_user.services.dto import EmployeeUserDto
from app.serializer_mapper import SerializerMapper
from ..serializers import EmployeeUserSerializer
from singleton_decorator import singleton

@singleton
class EmployeeUserSerializerMapper(SerializerMapper):
    def to_serializer(self, dto: EmployeeUserDto) -> EmployeeUserSerializer:
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