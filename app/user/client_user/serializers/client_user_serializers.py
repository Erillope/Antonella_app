from app.user.account.serializers import UserSerializer
from rest_framework import serializers

class ClientUserSerializer(UserSerializer):
    birthdate = serializers.DateField()