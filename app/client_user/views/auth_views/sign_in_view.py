from src.user.account import UserException
from src.user.client_user.services.dto import SignInDto
from app.validate import validate
from app.responses import success_response
from ...configuration import DependenciesManager
from ...serializers import SignInSerializer, ClienUserSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict

class SignInView(APIView):
    services = DependenciesManager.get_client_services()
    serializer_class = SignInSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.sign_in_service = self.services.construct_sign_in_service()
    
    @validate(SignInSerializer, UserException)
    def post(self, request: Request) -> Response:
        user_dto = self.sign_in_service.sign_in(self.__generate_dto(request.data))
        return success_response(ClienUserSerializer.generate_serializer(user_dto))
    
    def __generate_dto(self, data: Dict) -> SignInDto:
        return SignInDto(data.get('account'), data.get('password'))
    