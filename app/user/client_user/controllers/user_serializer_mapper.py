from ..serializers import ClientUserSerializer
from src.user.client_user.services.dto import ClientUserDto
from app.serializer_mapper import SerializerMapper
from singleton_decorator import singleton

@singleton
class UserSerializerMapper(SerializerMapper):
    def to_serializer(self, dto: ClientUserDto) -> ClientUserSerializer:
        data = {"id": dto.get_id(),
                "account": dto.get_account(),
                "name": dto.get_name(),
                "birthdate": dto.get_birthdate(),
                "status": dto.get_status().name,
                "joined_date": dto.get_joined_date().isoformat()
                }
        serializer = ClientUserSerializer(data=data)
        serializer.is_valid()
        return serializer