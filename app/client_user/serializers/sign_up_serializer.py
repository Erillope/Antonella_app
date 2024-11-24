from rest_framework import serializers
     
class SignUpSerializer(serializers.Serializer):
    account = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=250)
    birthdate = serializers.DateField()