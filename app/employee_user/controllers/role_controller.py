from app.employee_user.serializers import AddRoleSerializer, RemoveRoleSerializer, RoleSerializer
from src.user.account import UserException
from app.employee_user.configuration import DependenciesManager
from app.create_view import create_post, create_delete
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
    
    def generate_views(self) -> List:
        views = [
            ("add", create_post(AddRoleSerializer, UserException,
                                        lambda request: self.__add_role_executer(request), "Add Role")),
            ("remove/<str:role>", create_delete(UserException,
                                        lambda role: self.__remove_role_executer(role), "Remove Role")),
        ]
        return views