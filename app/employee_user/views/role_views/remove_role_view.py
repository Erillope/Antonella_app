from src.user.account import UserException
from src.user.employee_user.services.dto import RemoveRoleDto
from app.validate import validate
from app.responses import success_response
from ...configuration import DependenciesManager
from ...serializers import RemoveRoleSerializer, RoleSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict

class RemoveRoleView(APIView):
    services = DependenciesManager.get_employee_services()
    serializer_class = RemoveRoleSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.remove_role_service = self.services.construct_remove_role_service()
    
    @validate(RemoveRoleSerializer, UserException)
    def put(self, request: Request) -> Response:
        user_dto = self.remove_role_service.remove(self.__generate_dto(request.data))
        return success_response(RoleSerializer.generate_serializer(user_dto))

    def __generate_dto(self, data: Dict) -> RemoveRoleDto:
        return RemoveRoleDto(data.get('role'))