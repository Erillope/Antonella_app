from app.user.employee_user.serializers import AddRoleSerializer
from src.user.account import UserException
from app.user.employee_user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .employee_request_mapper import EmployeeRequestMapper
from .role_serializer_mapper import RoleSerializerMapper
from typing import List
from singleton_decorator import singleton

@singleton
class RoleController(Controller):
    services = DependenciesManager.get_employee_services()
    route_prefix = "role"
    
    def __init__(self) -> None:
        super().__init__()
        self.__request_mapper = EmployeeRequestMapper()
        self.__serializer_mapper = RoleSerializerMapper()
        
    def __add_role_view(self) -> ViewCreator:
        add_role_service = self.services.construct_add_role_service()
        executer = lambda request: add_role_service.add(
            self.__request_mapper.to_add_role_dto(request)
        )
        return ViewCreator(
                path = "add",
                serializer_class = AddRoleSerializer,
                exception_class = UserException,
                executer = executer,
                name = "Add Role",
                http_method = HttpMethod.POST,
                mapper = self.__serializer_mapper
            )
    
    def __remove_role_view(self) -> ViewCreator:
        remove_role_service = self.services.construct_remove_role_service()
        executer = lambda role: remove_role_service.remove(
            self.__request_mapper.to_remove_role_dto(role)
        ) 
        return ViewCreator(
                path = "remove/<str:role>",
                exception_class = UserException,
                executer = executer,
                name = "Remove Role",
                http_method = HttpMethod.DELETE,
                mapper = self.__serializer_mapper
            )
    
    def generate_views(self) -> List[ViewCreator]:
        views = [
            self.__add_role_view(),
            self.__remove_role_view()
        ]
        return views