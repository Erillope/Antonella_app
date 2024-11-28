from app.user.account.serializers import SignInSerializer, SignUpSerializer
from src.user.account import UserException
from app.user.client_user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .client_user_request_mapper import ClientUserRequestMapper
from .user_serializer_mapper import UserSerializerMapper
from typing import List
from singleton_decorator import singleton

@singleton
class AuthController(Controller):
    services = DependenciesManager.get_client_services()
    route_prefix = "auth"
    
    def __init__(self) -> None:
        super().__init__()
        self.__request_mapper = ClientUserRequestMapper()
        self.__serializer_mapper = UserSerializerMapper()
    
    def __sign_in_view(self) -> ViewCreator:
        sign_in_service = self.services.construct_sign_in_service()
        executer = lambda request: sign_in_service.sign_in(self.__request_mapper.to_sign_in_dto(request))
        return ViewCreator(
                path = "signin",
                serializer_class = SignInSerializer,
                exception_class = UserException,
                executer = executer,
                name = "Sign In",
                http_method = HttpMethod.POST,
                mapper = self.__serializer_mapper
            )
    
    def __sign_up_view(self) -> ViewCreator:
        sign_up_service = self.services.construct_sign_up_service()
        executer = lambda request: sign_up_service.sign_up(self.__request_mapper.to_sign_up_dto(request))
        return ViewCreator(
                path = "signup",
                serializer_class = SignUpSerializer,
                exception_class = UserException,
                executer = executer,
                name = "Sign Up",
                http_method = HttpMethod.POST,
                mapper = self.__serializer_mapper
            )
    
    def generate_views(self) -> List[ViewCreator]:
        views = [
            self.__sign_in_view(),
            self.__sign_up_view()
        ]
        return views