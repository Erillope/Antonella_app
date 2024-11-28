from rest_framework.request import Request
from app.user.account.account_request_mapper import AccountRequestMapper
from src.user.client_user.services.dto import ClientUserSignUpDto
from datetime import date
from singleton_decorator import singleton

@singleton
class ClientUserRequestMapper(AccountRequestMapper):
    def to_sign_up_dto(self, request: Request) -> ClientUserSignUpDto:
        return ClientUserSignUpDto(
            account = request.data.get('account'),
            name = request.data.get('name'),
            password = request.data.get('password'),
            birthdate = date.fromisoformat(request.data.get('birthdate'))
        )