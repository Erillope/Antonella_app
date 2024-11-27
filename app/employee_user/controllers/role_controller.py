from app.employee_user.serializers import AddRoleSerializer, RemoveRoleSerializer, RoleSerializer
from src.user.account import UserException
from app.employee_user.configuration import DependenciesManager
from app.create_view import ViewCreator, HttpMethod
from app.controller import Controller
from .request_adapter import RequestAdapter
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from typing import List

class RoleController(Controller):
    services = DependenciesManager.get_employee_services()
    route_prefix = "role"
    
    def __add_role_executer(self, request: Request) -> Serializer:
        add_role_service = self.services.construct_add_role_service()
        role_dto = add_role_service.add(RequestAdapter.to_add_role_dto(request))
        return RoleSerializer.generate_serializer(role_dto)
    
    def __remove_role_executer(self, role: str) -> Serializer:
        remove_role_service = self.services.construct_remove_role_service()
        role_dto = remove_role_service.remove(RequestAdapter.to_remove_role_dto(role))
        return RoleSerializer.generate_serializer(role_dto)
    
    def generate_views(self) -> List[ViewCreator]:
        views = [
            ViewCreator(
                path = "add",
                serializer_class = AddRoleSerializer,
                exception_class = UserException,
                executer = lambda request: self.__add_role_executer(request),
                name = "Add Role",
                http_method = HttpMethod.POST
            ),
            ViewCreator(
                path = "remove/<str:role>",
                exception_class = UserException,
                executer = lambda role: self.__remove_role_executer(role),
                name = "Remove Role",
                http_method = HttpMethod.DELETE
            )
        ]
        return views