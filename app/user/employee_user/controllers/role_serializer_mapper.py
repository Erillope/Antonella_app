from src.user.employee_user.services.dto import RoleDto
from app.serializer_mapper import SerializerMapper
from ..serializers import RoleSerializer
from singleton_decorator import singleton

@singleton
class RoleSerializerMapper(SerializerMapper):
    def to_serializer(self, dto: RoleDto) -> RoleSerializer:
        serializer = RoleSerializer(data={"role": dto.get_role()})
        serializer.is_valid()
        return serializer