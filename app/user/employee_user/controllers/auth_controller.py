from app.user.account.serializers import SignInSerializer
from app.user.employee_user.serializers import RegisterEmployeeSerializer
from src.user.account import UserException
from app.user.employee_user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .employee_request_mapper import EmployeeRequestMapper
from .employee_user_serializer_mapper import EmployeeUserSerializerMapper
from rest_framework.request import Request
from typing import List
from singleton_decorator import singleton

@singleton
class AuthController(Controller):
    services = DependenciesManager.get_employee_services()
    route_prefix = "auth"
    
    def __init__(self) -> None:
        super().__init__()
        self.__request_mapper = EmployeeRequestMapper()
        self.__serialier_mapper = EmployeeUserSerializerMapper()
        
    def __sign_in_view(self) -> ViewCreator:
        sign_in_service = self.services.construct_sign_in_service()
        executer = lambda request: sign_in_service.sign_in(
            self.__request_mapper.to_sign_in_dto(request)
        )
        return ViewCreator(
                path = "signin",
                serializer_class = SignInSerializer,
                exception_class = UserException,
                executer = executer,
                name = "Sign In",
                http_method = HttpMethod.POST,
                mapper = self.__serialier_mapper
            )
    
    def __register_view(self) -> ViewCreator:
        register_service = self.services.construct_register_service()
        executer = lambda request: register_service.register_employee(
            self.__request_mapper.to_register_dto(request)
        )
        return ViewCreator(
                path = "register",
                serializer_class = RegisterEmployeeSerializer,
                exception_class = UserException,
                executer = executer,
                name = "Register",
                http_method = HttpMethod.POST,
                mapper = self.__serialier_mapper
            )
    
    def generate_views(self) -> List[ViewCreator]:
        views = [
            self.__sign_in_view(),
            self.__register_view()
        ]
        return views