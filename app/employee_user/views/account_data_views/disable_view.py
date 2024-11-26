from src.user.account import UserException
from src.user.employee_user.services.dto import DisableDto
from app.validate import validate
from app.responses import success_response
from ...configuration import DependenciesManager
from ...serializers import DisableSerializer, EmployeeUserSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict

class DisableView(APIView):
    services = DependenciesManager.get_employee_services()
    serializer_class = DisableSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.disable_account_service = self.services.construct_disable_account_service()
    
    @validate(DisableSerializer, UserException)
    def put(self, request: Request) -> Response:
        user_dto = self.disable_account_service.disable(self.__generate_dto(request.data))
        return success_response(EmployeeUserSerializer.generate_serializer(user_dto))

    def __generate_dto(self, data: Dict) -> DisableDto:
        return DisableDto(data.get('id'))