from rest_framework.request import Request
from src.user.account.services.dto import SignInDto, SignUpDto, ChangeDataDto, EnableDto, DisableDto

class AccountRequestMapper:
    def to_sign_in_dto(self, request: Request) -> SignInDto:
        return SignInDto(
            account = request.data.get('account'),
            password = request.data.get('password')
            )
    
    def to_sign_up_dto(self, request: Request) -> SignUpDto:
        return SignUpDto(
            account = request.data.get('account'),
            name = request.data.get('name'),
            password = request.data.get('password'),
            )
    
    def to_change_data_dto(self, request: Request) -> ChangeDataDto:
        return ChangeDataDto(
            id = request.data.get('id'),
            account = request.data.get('account'),
            name = request.data.get('name'),
            password = request.data.get('password')
        )
    
    def to_enable_dto(self, request: Request) -> EnableDto:
        return EnableDto(id = request.data.get('id'))

    def to_disable_dto(self, request: Request) -> DisableDto:
        return DisableDto(id = request.data.get('id'))