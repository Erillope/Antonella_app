from app.user.account.serializers import ChangeDataSerializer, EnableSerializer, DisableSerializer
from src.user.account import UserException
from app.user.client_user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .client_user_request_mapper import ClientUserRequestMapper
from .user_serializer_mapper import UserSerializerMapper
from typing import List
from singleton_decorator import singleton

@singleton
class AccountDataController(Controller):
    services = DependenciesManager.get_client_services()
    route_prefix = "account"
    
    def __init__(self) -> None:
        super().__init__()
        self.__request_mapper = ClientUserRequestMapper()
        self.__serializer_mapper = UserSerializerMapper()
        
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
    
    def generate_views(self) -> List[ViewCreator]:
        views = [
            self.__change_data_view(),
            self.__enable_view(),
            self.__disable_view(),
        ]
        return views