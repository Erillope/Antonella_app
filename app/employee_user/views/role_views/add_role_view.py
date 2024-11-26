from src.user.account import UserException
from src.user.employee_user.services.dto import AddRoleDto
from app.validate import validate
from app.responses import success_response
from ...configuration import DependenciesManager
from ...serializers import AddRoleSerializer, RoleSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict

class AddRoleView(APIView):
    services = DependenciesManager.get_employee_services()
    serializer_class = AddRoleSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.add_role_service = self.services.construct_add_role_service()
    
    @validate(AddRoleSerializer, UserException)
    def put(self, request: Request) -> Response:
        user_dto = self.add_role_service.add(self.__generate_dto(request.data))
        return success_response(RoleSerializer.generate_serializer(user_dto))

    def __generate_dto(self, data: Dict) -> AddRoleDto:
        return AddRoleDto(data.get('role'))