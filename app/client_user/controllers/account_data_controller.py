from app.client_user.serializers import (ChangeDataSerializer, EnableSerializer, 
                                         DisableSerializer, ClienUserSerializer)
from src.user.account import UserException
from app.client_user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .request_adapter import RequestAdapter
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from typing import List

class AccountDataController(Controller):
    services = DependenciesManager.get_client_services()
    route_prefix = "account"
    
    def __change_data_executer(self, request: Request):
        change_data_service = self.services.construct_change_data_service()
        user_dto = change_data_service.change_data(RequestAdapter.to_change_data_dto(request))
        return ClienUserSerializer.generate_serializer(user_dto)
    
    def __enable_executer(self, request: Request):
        enable_account_service = self.services.construct_enable_account_service()
        user_dto = enable_account_service.enable(RequestAdapter.to_enable_dto(request))
        return ClienUserSerializer.generate_serializer(user_dto)
    
    def __disable_executer(self, request: Request) -> Serializer:
        disable_account_service = self.services.construct_disable_account_service()
        user_dto = disable_account_service.disable(RequestAdapter.to_disable_dto(request))
        return ClienUserSerializer.generate_serializer(user_dto)
    
    def generate_views(self) -> List:
        views = [
            ViewCreator(
                path = "change_data",
                exception_class = UserException,
                executer = lambda request: self.__change_data_executer(request),
                name = "Change Data",
                serializer_class = ChangeDataSerializer,
                http_method = HttpMethod.PUT
            ),
            ViewCreator(
                path = "enable",
                exception_class = UserException,
                executer = lambda request: self.__enable_executer(request),
                name = "Enable",
                serializer_class = EnableSerializer,
                http_method = HttpMethod.PUT
            ),
            ViewCreator(
                path = "disable",
                exception_class = UserException,
                executer = lambda request: self.__disable_executer(request),
                name = "Disable",
                serializer_class = DisableSerializer,
                http_method = HttpMethod.PUT
            ),
        ]
        return views