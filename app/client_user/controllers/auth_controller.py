from app.client_user.serializers import SignInSerializer, SignUpSerializer, ClienUserSerializer
from src.user.account import UserException
from app.client_user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .request_adapter import RequestAdapter
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from typing import List

class AuthController(Controller):
    services = DependenciesManager.get_client_services()
    route_prefix = "auth"
    
    def __sign_in_executer(self, request: Request) -> Serializer:
        sign_in_service = self.services.construct_sign_in_service()
        user_dto = sign_in_service.sign_in(RequestAdapter.to_sign_in_dto(request))
        return ClienUserSerializer.generate_serializer(user_dto)
    
    def __sign_up_executer(self, request: Request) -> Serializer:
        sign_up_service = self.services.construct_sign_up_service()
        user_dto = sign_up_service.sign_up(RequestAdapter.to_sign_up_dto(request))
        return ClienUserSerializer.generate_serializer(user_dto)
    
    def generate_views(self) -> List:
        views = [
            ViewCreator(
                path = "signin",
                serializer_class = SignInSerializer,
                exception_class = UserException,
                executer = lambda request: self.__sign_in_executer(request),
                name = "Sign In",
                http_method = HttpMethod.POST
            ),
            ViewCreator(
                path = "signup",
                serializer_class = SignUpSerializer,
                exception_class = UserException,
                executer = lambda request: self.__sign_up_executer(request),
                name = "Sign Up",
                http_method = HttpMethod.POST
            ),
        ]
        return views