from app.user.serializers import (ChangeDataSerializer, EnableSerializer,
                                  DisableSerializer, GiveRoleSerializer, FilterUserSerializer)
from app.user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .user_request_mapper import UserRequestMapper
from .user_serializer_mapper import UserSerializerMapper, GetListUserSerializerMapper
from typing import List

class AccountDataController(Controller):
    services = DependenciesManager.get_user_services()
    route_prefix = "account"
    
    def __init__(self) -> None:
        super().__init__()
        self.__request_mapper = UserRequestMapper()
        self.__serializer_mapper = UserSerializerMapper()
        
    def __change_data_view(self) -> ViewCreator:
        change_data_service = self.services.construct_change_data_service()
        executer = lambda request: change_data_service.change_data(
            self.__request_mapper.to_change_data_dto(request)
            )
        return ViewCreator(
                path = "change_data",
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
                executer = executer,
                name = "Disable",
                serializer_class = DisableSerializer,
                http_method = HttpMethod.PUT,
                mapper = self.__serializer_mapper
            )
    
    def __give_role_view(self) -> ViewCreator:
        give_role_service = self.services.construct_give_role_service()
        executer = lambda request: give_role_service.give(self.__request_mapper.to_give_role_dto(request))
        return ViewCreator(
            path = "give_role",
            executer = executer,
            name = "Give Role",
            serializer_class = GiveRoleSerializer,
            http_method = HttpMethod.POST,
            mapper = self.__serializer_mapper
        )
    
    def __remove_role_view(self) -> ViewCreator:
        remove_role_service = self.services.construct_remove_role_service()
        executer = lambda id, roles: remove_role_service.remove(
            self.__request_mapper.to_remove_role_dto(id, roles)
            )
        return ViewCreator(
            path = "remove_role/<str:id>/<str:roles>",
            executer = executer,
            name = "Remove Role",
            http_method = HttpMethod.DELETE,
            mapper = self.__serializer_mapper
        )
    
    def __expresion_filter_user_view(self) -> ViewCreator:
        filter_user_service = self.services.construct_filter_user_service()
        executer = lambda expresion, order_by, offset, limit, direction: filter_user_service.filter(
            self.__request_mapper.to_filter_user_dto(expresion, order_by, offset, limit, direction)
            )
        return ViewCreator(
            path = "filter/<str:expresion>/<str:order_by>/<int:offset>/<int:limit>/<str:direction>",
            executer = executer,
            name = "Filter User",
            http_method = HttpMethod.GET,
            mapper = GetListUserSerializerMapper()
        )
    
    def __filter_user_view(self) -> ViewCreator:
        filter_user_service = self.services.construct_filter_user_service()
        executer = lambda order_by, offset, limit, direction: filter_user_service.filter(
            self.__request_mapper.to_filter_user_dto(None, order_by, offset, limit, direction)
            )
        return ViewCreator(
            path = "filter/<str:order_by>/<int:offset>/<int:limit>/<str:direction>",
            executer = executer,
            name = "Filter User",
            http_method = HttpMethod.GET,
            mapper = GetListUserSerializerMapper()
        )
        
    def generate_views(self) -> List[ViewCreator]:
        views = [
            self.__change_data_view(),
            self.__enable_view(),
            self.__disable_view(),
            self.__give_role_view(),
            self.__remove_role_view(),
            self.__filter_user_view(),
            self.__expresion_filter_user_view()
        ]
        return views