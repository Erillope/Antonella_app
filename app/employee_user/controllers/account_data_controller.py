from app.employee_user.serializers import (ChangeDataSerializer, EnableSerializer, DisableSerializer,
                                           GiveRoleSerializer, TakeRoleSerializer, EmployeeUserSerializer)
from src.user.account import UserException
from app.employee_user.configuration import DependenciesManager
from app.create_view import create_put
from app.controller import Controller
from .request_adapter import RequestAdapter
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from typing import List

class AccountDataController(Controller):
    services = DependenciesManager.get_employee_services()
    route_prefix = "account"
    
    def __change_data_executer(self, request: Request):
        change_data_service = self.services.construct_change_data_service()
        employee_dto = change_data_service.change_data(RequestAdapter.to_change_data_dto(request))
        return EmployeeUserSerializer.generate_serializer(employee_dto)
    
    def __enable_executer(self, request: Request):
        enable_account_service = self.services.construct_enable_account_service()
        employee_dto = enable_account_service.enable(RequestAdapter.to_enable_dto(request))
        return EmployeeUserSerializer.generate_serializer(employee_dto)
    
    def __disable_executer(self, request: Request) -> Serializer:
        disable_account_service = self.services.construct_disable_account_service()
        employee_dto = disable_account_service.disable(RequestAdapter.to_disable_dto(request))
        return EmployeeUserSerializer.generate_serializer(employee_dto)
    
    def __give_role_executer(self, request: Request) -> Serializer:
        give_role_service = self.services.construct_give_role_service()
        employee_dto = give_role_service.give(RequestAdapter.to_give_role_dto(request))
        return EmployeeUserSerializer.generate_serializer(employee_dto)
    
    def __take_role_executer(self, request: Request) -> Serializer:
        take_role_service = self.services.construct_take_role_service()
        employee_dto = take_role_service.take(RequestAdapter.to_take_role_dto(request))
        return EmployeeUserSerializer.generate_serializer(employee_dto)
    
    def generate_views(self) -> List:
        views = [
            ("change_data", create_put(ChangeDataSerializer, UserException,
                                        lambda request: self.__change_data_executer(request), "Change Data")),
            ("enable", create_put(EnableSerializer, UserException,
                                   lambda request: self.__enable_executer(request), "Enable")),
            ("disable", create_put(DisableSerializer, UserException,
                                    lambda request: self.__disable_executer(request), "Disable")),
            ("give_role", create_put(GiveRoleSerializer, UserException,
                                    lambda request: self.__give_role_executer(request), "Give Role")),
            ("take_role", create_put(TakeRoleSerializer, UserException,
                                    lambda request: self.__take_role_executer(request), "Tale Role")),
        ]
        return views