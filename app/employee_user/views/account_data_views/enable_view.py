from src.user.account import UserException
from src.user.employee_user.services.dto import EnableDto
from app.validate import validate
from app.responses import success_response
from ...configuration import DependenciesManager
from ...serializers import EnableSerializer, EmployeeUserSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict

class EnableView(APIView):
    services = DependenciesManager.get_employee_services()
    serializer_class = EnableSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.enable_account_service = self.services.construct_enable_account_service()
    
    @validate(EnableSerializer, UserException)
    def put(self, request: Request) -> Response:
        user_dto = self.enable_account_service.enable(self.__generate_dto(request.data))
        return success_response(EmployeeUserSerializer.generate_serializer(user_dto))
    
    def __generate_dto(self, data: Dict) -> EnableDto:
        return EnableDto(data.get('id'))