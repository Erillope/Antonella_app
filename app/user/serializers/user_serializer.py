from src.user.domain import AccountStatus
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    account = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=25)
    status = serializers.ChoiceField(choices=[(s.name, s.name) for s in AccountStatus])
    birthdate = serializers.DateField()
    roles = serializers.ListField(
        child=serializers.CharField(max_length=25),
        allow_empty=False)
    created_date = serializers.DateField()

class GetListUserSerializer(serializers.Serializer):
    users = serializers.ListField(child=UserSerializer())