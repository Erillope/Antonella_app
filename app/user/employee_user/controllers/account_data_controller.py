from app.user.account.serializers import ChangeDataSerializer, EnableSerializer, DisableSerializer
from app.user.employee_user.serializers import GiveRoleSerializer, TakeRoleSerializer
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
class AccountDataController(Controller):
    services = DependenciesManager.get_employee_services()
    route_prefix = "account"
    
    def __init__(self) -> None:
        super().__init__()
        self.__request_mapper = EmployeeRequestMapper()
        self.__serializer_mapper = EmployeeUserSerializerMapper()
        
    def __change_data_view(self) -> ViewCreator:
        change_data_service = self.services.construct_change_data_service()
        executer = lambda request: change_data_service.change_data(
            self.__request_mapper.to_change_data_dto(request)
            )
        return ViewCreator(
                path = "change_data",
                exception_class = UserException,
                executer = executer,
                name = "Change Data",
                serializer_class = ChangeDataSerializer,
                http_method = HttpMethod.PUT,
                mapper = self.__serializer_mapper
            )
    
    def __enable_view(self) -> ViewCreator:
        enable_account_service = self.services.construct_enable_account_service()
        executer = lambda request: enable_account_service.enable(
            self.__request_mapper.to_enable_dto(request)
            )
        return ViewCreator(
                path = "enable",
                exception_class = UserException,
                executer = executer,
                name = "Enable",
                serializer_class = EnableSerializer,
                http_method = HttpMethod.PUT,
                mapper = self.__serializer_mapper
            )
    
    def __disable_view(self) -> ViewCreator:
        disable_account_service = self.services.construct_disable_account_service()
        executer = lambda request: disable_account_service.disable(
            self.__request_mapper.to_disable_dto(request)
            )
        return ViewCreator(
                path = "disable",
                exception_class = UserException,
                executer = executer,
                name = "Disable",
                serializer_class = DisableSerializer,
                http_method = HttpMethod.PUT,
                mapper = self.__serializer_mapper
            )
    
    def __give_role_view(self) -> ViewCreator:
        give_role_service = self.services.construct_give_role_service()
        executer = lambda request: give_role_service.give(
            self.__request_mapper.to_give_role_dto(request)
        )
        return ViewCreator(
                path = "give_role",
                exception_class = UserException,
                executer = executer,
                name = "Give Role",
                serializer_class = GiveRoleSerializer,
                http_method = HttpMethod.PUT,
                mapper = self.__serializer_mapper
            )
    
    def __take_role_view(self) -> ViewCreator:
        take_role_service = self.services.construct_take_role_service()
        executer = lambda request: take_role_service.take(
            self.__request_mapper.to_take_role_dto(request)
        )
        return ViewCreator(
                path = "take_role",
                exception_class = UserException,
                executer = executer,
                name = "Take Role",
                serializer_class = TakeRoleSerializer,
                http_method = HttpMethod.PUT,
                mapper = self.__serializer_mapper
            )
    
    def generate_views(self) -> List[ViewCreator]:
        views = [
            self.__change_data_view(),
            self.__enable_view(),
            self.__disable_view(),
            self.__give_role_view(),
            self.__take_role_view()
        ]
        return views