from ..serializers import RoleSerializer, GetListRoleSerializer
from src.user.services.dto import RoleDto
from app.serializer_mapper import SerializerMapper
from typing import List

class RoleSerializerMapper(SerializerMapper):
    def to_serializer(self, dto: RoleDto) -> RoleSerializer:
        data = {"role": dto.get_role(),
                "created_date": dto.get_created_date().isoformat()
                }
        serializer = RoleSerializer(data=data)
        serializer.is_valid()
        return serializer

class GetListRoleSerializerMapper(SerializerMapper):
    def __init__(self) -> None:
        self.__role_serializer_mapper = RoleSerializerMapper()
        
    def to_serializer(self, dto: List[RoleDto]) -> GetListRoleSerializer:
        data = {
            "roles": [self.__role_serializer_mapper.to_serializer(role_dto).data for role_dto in dto]
        }
        serializer = GetListRoleSerializer(data=data)
        serializer.is_valid()
        return serializer