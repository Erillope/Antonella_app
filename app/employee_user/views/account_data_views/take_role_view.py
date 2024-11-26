from src.user.account import UserException
from src.user.employee_user.services.dto import TakeRoleDto
from app.validate import validate
from app.responses import success_response
from ...configuration import DependenciesManager
from ...serializers import TakeRoleSerializer, EmployeeUserSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict

class TakeRoleView(APIView):
    services = DependenciesManager.get_employee_services()
    serializer_class = TakeRoleSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.take_role_service = self.services.construct_take_role_service()
    
    @validate(TakeRoleSerializer, UserException)
    def put(self, request: Request) -> Response:
        user_dto = self.take_role_service.take(self.__generate_dto(request.data))
        return success_response(EmployeeUserSerializer.generate_serializer(user_dto))
    
    def __generate_dto(self, data: Dict) -> TakeRoleDto:
        return TakeRoleDto(data.get('id'), set(data.get('roles')))