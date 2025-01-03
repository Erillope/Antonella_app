from ..serializers import UserSerializer, GetListUserSerializer
from src.user.services.dto import UserAccountDto
from app.common.serializer_mapper import SerializerMapper
from typing import List

class UserSerializerMapper(SerializerMapper):
    def to_serializer(self, dto: UserAccountDto) -> UserSerializer:
        data = {"id": dto.get_id(),
                "account": dto.get_account(),
                "name": dto.get_name(),
                "birthdate": dto.get_birthdate(),
                "status": dto.get_status().name,
                "roles": dto.get_roles(),
                "created_date": dto.get_created_date().isoformat()
                }
        serializer = UserSerializer(data=data)
        serializer.is_valid()
        return serializer

class GetListUserSerializerMapper(SerializerMapper):
    def __init__(self) -> None:
        self.__user_serializer_mapper = UserSerializerMapper()
        
    def to_serializer(self, dto: List[UserAccountDto]) -> GetListUserSerializer:
        data = {
            "users": [self.__user_serializer_mapper.to_serializer(user_dto).data for user_dto in dto]
        }
        serializer = GetListUserSerializer(data=data)
        serializer.is_valid()
        return serializer