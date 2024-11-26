from src.user.employee_user.services.dto import RegisterEmployeeDto
from src.user.account import UserException
from app.responses import success_response
from app.validate import validate
from ...serializers import RegisterEmployeeSerializer, EmployeeUserSerializer
from ...configuration import DependenciesManager
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict
from datetime import date

class RegisterEmployeeView(APIView):
    services = DependenciesManager.get_employee_services()
    serializer_class = RegisterEmployeeSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.register_service = self.services.construct_register_service()
    
    @validate(RegisterEmployeeSerializer, UserException)
    def post(self, request: Request) -> Response:
        employee_dto = self.register_service.register_employee(self.__generate_dto(request.data))
        return success_response(EmployeeUserSerializer.generate_serializer(employee_dto))
        
    def __generate_dto(self, data: Dict) -> RegisterEmployeeDto:
        return RegisterEmployeeDto(data.get('account'), data.get('name'), set(data.get('roles')))