from app.user.serializers import GetListUserSerializer
from app.common.serializer_mapper import SerializerMapper
from src.user.services.dto import UserAccountDto
from .user_serializer_mapper import UserSerializerMapper
from typing import List

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