from app.user.serializers import (ChangeDataSerializer, EnableSerializer, GetListUserSerializer,
                                  DisableSerializer, GiveRoleSerializer, UserSerializer)
from app.user.configuration import DependenciesManager
from app.common.controller import Controller
from .user_request_mapper import UserRequestMapper
from .user_serializer_mapper import UserSerializerMapper, GetListUserSerializerMapper

class AccountDataController(Controller):
    controller_route = "account"
    services = DependenciesManager.get_user_services()
    request_mapper = UserRequestMapper()
    serializer_mapper = UserSerializerMapper()
    list_serializer_mapper = GetListUserSerializerMapper()
    
    @Controller.put("change_data", "Change Data", ChangeDataSerializer)
    def change_data(cls, request: ChangeDataSerializer) -> UserSerializer:
        change_data_service = cls.services.construct_change_data_service()
        dto = change_data_service.change_data(cls.request_mapper.to_change_data_dto(request))
        return cls.serializer_mapper.to_serializer(dto)
    
    @Controller.put("enable", "Enable", EnableSerializer)
    def enable(cls, request: EnableSerializer) -> UserSerializer:
        enable_account_service = cls.services.construct_enable_account_service()
        dto = enable_account_service.enable(cls.request_mapper.to_enable_dto(request))
        return cls.serializer_mapper.to_serializer(dto) 
    
    @Controller.put("disable", "Disable", DisableSerializer)
    def disable(cls, request: DisableSerializer) -> UserSerializer:
        disable_account_service = cls.services.construct_disable_account_service()
        dto = disable_account_service.disable(cls.request_mapper.to_disable_dto(request))
        return cls.serializer_mapper.to_serializer(dto)
    
    @Controller.post("give_role", "Give Role", GiveRoleSerializer)
    def give_role(cls, request: GiveRoleSerializer) -> UserSerializer:
        give_role_service = cls.services.construct_give_role_service()
        dto = give_role_service.give(cls.request_mapper.to_give_role_dto(request))
        return cls.serializer_mapper.to_serializer(dto)
    
    @Controller.delete("remove_role/<str:id>/<str:roles>", "Remove Role")
    def remove_role(cls, id: str, roles: str) -> UserSerializer:
        remove_role_service = cls.services.construct_remove_role_service()
        dto = remove_role_service.remove(cls.request_mapper.to_remove_role_dto(id, roles))
        return cls.serializer_mapper.to_serializer(dto)
    
    @Controller.get("filter/<str:order_by>/<int:offset>/<int:limit>/<str:direction>", "Filter User")
    def filter_user(cls, order_by: str, offset: int, limit: int, direction: str) -> GetListUserSerializer:
        filter_user_service = cls.services.construct_filter_user_service()
        dtos = filter_user_service.filter(cls.request_mapper.to_filter_user_dto(None, order_by, offset, limit, direction))
        return cls.list_serializer_mapper.to_serializer(dtos)
    
    @Controller.get("filter/<str:expresion>/<str:order_by>/<int:offset>/<int:limit>/<str:direction>", "Filter User")
    def expresion_filter_user(cls, expresion: str, order_by: str, offset: int, limit: int, direction: str) -> GetListUserSerializer:
        filter_user_service = cls.services.construct_filter_user_service()
        dtos = filter_user_service.filter(cls.request_mapper.to_filter_user_dto(expresion, order_by, offset, limit, direction))
        return cls.list_serializer_mapper.to_serializer(dtos)