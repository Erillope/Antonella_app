from src.user.account import AccountStatus
from src.user.client_user.services.dto import ClientUserDto
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    account = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=25)
    status = serializers.ChoiceField(choices=[(s.name, s.name) for s in AccountStatus])
    joined_date = serializers.DateField()