from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status
from typing import Dict

def success_response(serializer: Serializer) -> Response:
    return Response({
        "status": "success",
        "code": 200,
        "data": serializer.data
    }, status = status.HTTP_200_OK)

def failure_response(e: Exception) -> Response:
    return Response({
        "status": "failure",
        "code": 400,
        "message": str(e)
    }, status = status.HTTP_400_BAD_REQUEST)

def invalid_field_response(errors: Dict) -> Response:
    msg = "Asegurese de llenar correctamente los campos requeridos: " + str(list(errors.keys()))
    e = Exception(msg)
    return failure_response(e)

def internal_server_error_response() -> Response:
    return Response({
        "status": "failure",
        "code": 500,
        "message": "Internal Server Error"
    }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)