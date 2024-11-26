from src.user.account import UserException
from src.user.employee_user.services.dto import ChangeDataDto
from app.validate import validate
from app.responses import success_response
from ...configuration import DependenciesManager
from ...serializers import ChangeDataSerializer, EmployeeUserSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from typing import Any, Dict

class ChangeDataView(APIView):
    services = DependenciesManager.get_employee_services()
    serializer_class = ChangeDataSerializer
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.change_data_service = self.services.construct_change_data_service()
    
    @validate(ChangeDataSerializer, UserException)
    def put(self, request: Request) -> Response:
        user_dto = self.change_data_service.change_data(self.__generate_dto(request.data))
        return success_response(EmployeeUserSerializer.generate_serializer(user_dto))
    
    def __generate_dto(self, data: Dict) -> ChangeDataDto:
        return ChangeDataDto(data.get('id'), data.get("account"), data.get('name'), data.get('password'))