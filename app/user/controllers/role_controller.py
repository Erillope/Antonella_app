from app.user.serializers import AddRoleSerializer, RenameRoleSerializer
from app.user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .user_request_mapper import UserRequestMapper
from .role_serializer_mapper import RoleSerializerMapper, GetListRoleSerializerMapper
from typing import List

class RoleController(Controller):
    services = DependenciesManager.get_role_services()
    route_prefix = "role"
    
    def __init__(self) -> None:
        self.__request_mapper = UserRequestMapper()
        self.__serializer_mapper = RoleSerializerMapper()
    
    def __add_role_view(self) -> ViewCreator:
        add_role_service = self.services.construct_add_role_service()
        executer = lambda request: add_role_service.add(self.__request_mapper.to_add_role_dto(request))
        return ViewCreator(
                path = "add",
                serializer_class = AddRoleSerializer,
                executer = executer,
                name = "Add Role",
                http_method = HttpMethod.POST,
                mapper = self.__serializer_mapper
            )
    
    def __delete_role_view(self) -> ViewCreator:
        delete_role_service = self.services.construct_delete_role_service()
        executer = lambda role: delete_role_service.delete(self.__request_mapper.to_delete_role_dto(role))
        return ViewCreator(
            path = "delete/<str:role>",
            executer = executer,
            name = "Delete Role",
            http_method = HttpMethod.DELETE,
            mapper = self.__serializer_mapper
        )
    
    def __rename_role_view(self) -> ViewCreator:
        rename_role_service = self.services.construct_rename_role_service()
        executer = lambda request: rename_role_service.rename(
            self.__request_mapper.to_rename_role_dto(request)
            ) 
        return ViewCreator(
            path = "rename",
            serializer_class = RenameRoleSerializer,
            executer = executer,
            name = "Rename Role",
            http_method = HttpMethod.PUT,
            mapper = self.__serializer_mapper
        )
        
    def __get_all_roles_view(self) -> ViewCreator:
        get_all_roles_service = self.services.construct_get_all_roles_service()
        executer = lambda : get_all_roles_service.get_all()
        return ViewCreator(
            path = "",
            executer = executer,
            name = "Add Role",
            http_method = HttpMethod.GET,
            mapper = GetListRoleSerializerMapper()
        )
        
    def generate_views(self) -> List[ViewCreator]:
        return [
            self.__add_role_view(),
            self.__delete_role_view(),
            self.__get_all_roles_view(),
            self.__rename_role_view()
        ]