from src.user.account import AccountStatus
from src.user.client_user.services.dto import ClientUserDto
from rest_framework import serializers

class ClienUserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    account = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=25)
    birthdate = serializers.DateField()
    status = serializers.ChoiceField(choices=[(s.name, s.name) for s in AccountStatus])
    joined_date = serializers.DateField()
    
    @staticmethod
    def generate_serializer(dto: ClientUserDto) -> "ClienUserSerializer":
        data = {"id": dto.get_id(),
                "account": dto.get_account(),
                "name": dto.get_name(),
                "birthdate": dto.get_birthdate(),
                "status": dto.get_status().name,
                "joined_date": dto.get_joined_date().isoformat()
                }
        serializer = ClienUserSerializer(data=data)
        serializer.is_valid()
        return serializer
        