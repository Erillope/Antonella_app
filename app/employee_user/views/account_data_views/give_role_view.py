from src.user.account import UserException
from src.user.employee_user.services.dto import GiveRoleDto
from app.validate import validate
from app.responses import success_response
from ...configuration import DependenciesManager
from ...serializers import GiveRoleSerializer, EmployeeUserSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict

class GiveRoleView(APIView):
    services = DependenciesManager.get_employee_services()
    serializer_class = GiveRoleSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.give_role_service = self.services.construct_give_role_service()
    
    @validate(GiveRoleSerializer, UserException)
    def put(self, request: Request) -> Response:
        user_dto = self.give_role_service.give(self.__generate_dto(request.data))
        return success_response(EmployeeUserSerializer.generate_serializer(user_dto))
    
    def __generate_dto(self, data: Dict) -> GiveRoleDto:
        return GiveRoleDto(data.get('id'), set(data.get('roles')))