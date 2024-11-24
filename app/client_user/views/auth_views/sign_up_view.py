from src.user.client_user.services.dto import SignUpDto
from src.user.account import UserException
from app.responses import success_response
from app.validate import validate
from ...serializers import SignUpSerializer, ClienUserSerializer
from ...configuration import DependenciesManager
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict
from datetime import date

class SignUpView(APIView):
    services = DependenciesManager.get_client_services()
    serializer_class = SignUpSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.sign_up_service = self.services.construct_sign_up_service()
    
    @validate(SignUpSerializer, UserException)
    def post(self, request: Request) -> Response:
        user_dto = self.sign_up_service.sign_up(self.__generate_dto(request.data))
        return success_response(ClienUserSerializer.generate_serializer(user_dto))
        
    def __generate_dto(self, data: Dict) -> SignUpDto:
        return SignUpDto(data.get('account'), data.get('name'), data.get('password'),
                         date.fromisoformat(data.get('birthdate')))