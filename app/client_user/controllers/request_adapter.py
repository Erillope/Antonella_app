from rest_framework.request import Request
from src.user.client_user.services.dto import SignInDto, SignUpDto, ChangeDataDto, EnableDto, DisableDto
from datetime import date

class RequestAdapter:
    @staticmethod
    def to_sign_in_dto(request: Request) -> SignInDto:
        return SignInDto(
            account = request.data.get('account'),
            password = request.data.get('password')
            )
    
    @staticmethod
    def to_sign_up_dto(request: Request) -> SignUpDto:
        return SignUpDto(
            account = request.data.get('account'),
            name = request.data.get('name'),
            password = request.data.get('password'),
            birthdate = date.fromisoformat(request.data.get('birthdate'))
            )
    
    @staticmethod
    def to_change_data_dto(request: Request) -> ChangeDataDto:
        return ChangeDataDto(
            id = request.data.get('id'),
            account = request.data.get('account'),
            name = request.data.get('name'),
            password = request.data.get('password')
        )
    
    @staticmethod
    def to_enable_dto(request: Request) -> EnableDto:
        return EnableDto(id = request.data.get('id'))
    
    @staticmethod
    def to_disable_dto(request: Request) -> DisableDto:
        return DisableDto(id = request.data.get('id'))