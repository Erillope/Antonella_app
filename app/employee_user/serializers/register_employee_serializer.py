from rest_framework import serializers
     
class RegisterEmployeeSerializer(serializers.Serializer):
    account = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=25)
    roles = serializers.ListField(
        child=serializers.CharField(max_length=25),
        allow_empty=False)