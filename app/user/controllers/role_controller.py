from app.user.serializers import AddRoleSerializer, RenameRoleSerializer, RoleSerializer, GetListRoleSerializer
from app.user.configuration import DependenciesManager
from app.common.controller import Controller
from .user_request_mapper import UserRequestMapper
from .role_serializer_mapper import RoleSerializerMapper, GetListRoleSerializerMapper

class RoleController(Controller):
    controller_route = "role"
    services = DependenciesManager.get_role_services()
    request_mapper = UserRequestMapper()
    serializer_mapper = RoleSerializerMapper()
    list_serializer_mapper = GetListRoleSerializerMapper()
    
    @Controller.post("add", "Add Role", AddRoleSerializer)
    def add(cls, request: AddRoleSerializer) -> RoleSerializer:
        add_role_service = cls.services.construct_add_role_service()
        dto = add_role_service.add(cls.request_mapper.to_add_role_dto(request))
        return cls.serializer_mapper.to_serializer(dto)
    
    @Controller.delete("delete/<str:role>", "Delete Role")
    def delete(cls, role: str) -> RoleSerializer:
        delete_role_service = cls.services.construct_delete_role_service()
        dto = delete_role_service.delete(cls.request_mapper.to_delete_role_dto(role))
        return cls.serializer_mapper.to_serializer(dto)
    
    @Controller.put("rename", "Rename Role", RenameRoleSerializer)
    def rename(cls, request: RenameRoleSerializer) -> RoleSerializer:
        rename_role_service = cls.services.construct_rename_role_service()
        dto = rename_role_service.rename(cls.request_mapper.to_rename_role_dto(request))
        return cls.serializer_mapper.to_serializer(dto)
    
    @Controller.get("", "Get All Roles")
    def get_all(cls) -> GetListRoleSerializer:
        get_all_roles_service = cls.services.construct_get_all_roles_service()
        dtos = get_all_roles_service.get_all()
        return cls.list_serializer_mapper.to_serializer(dtos)