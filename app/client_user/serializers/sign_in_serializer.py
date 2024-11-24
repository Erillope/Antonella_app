from rest_framework import serializers

class SignInSerializer(serializers.Serializer):
    account = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=250)