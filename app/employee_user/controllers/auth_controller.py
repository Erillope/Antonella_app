from app.employee_user.serializers import SignInSerializer, RegisterEmployeeSerializer, EmployeeUserSerializer
from src.user.account import UserException
from app.employee_user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .request_adapter import RequestAdapter
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from typing import List

class AuthController(Controller):
    services = DependenciesManager.get_employee_services()
    route_prefix = "auth"
    
    def __sign_in_executer(self, request: Request) -> Serializer:
        sign_in_service = self.services.construct_sign_in_service()
        employee_dto = sign_in_service.sign_in(RequestAdapter.to_sign_in_dto(request))
        return EmployeeUserSerializer.generate_serializer(employee_dto)
    
    def __register_executer(self, request: Request) -> Serializer:
        register_service = self.services.construct_register_service()
        employee_dto = register_service.register_employee(RequestAdapter.to_register_dto(request))
        return EmployeeUserSerializer.generate_serializer(employee_dto)
    
    def generate_views(self) -> List[ViewCreator]:
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
                path = "register",
                serializer_class = RegisterEmployeeSerializer,
                exception_class = UserException,
                executer = lambda request: self.__register_executer(request),
                name = "Register",
                http_method = HttpMethod.POST
            )
        ]
        return views