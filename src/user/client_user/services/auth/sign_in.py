from ...data_providers import ClientUserRepository
from ...domain import ClientUser
from ..dto import SignInDto, ClientUserDto, EnableDto
from ..user_is_registered import UserIsRegistered
from ..account_data import IEnableClientUserAccount
from ..exception import IncorrectPasswordException
from .ISign_in import ISingIn
from typing import override

class SignIn(ISingIn):
    def __init__(self, user_repository: ClientUserRepository, enable_account_service: IEnableClientUserAccount) -> None:
        self.__user_repository = user_repository
        self.__enable_account_service = enable_account_service
        
    @override
    def sign_in(self, dto: SignInDto) -> ClientUserDto:
        user = UserIsRegistered.is_registered_by_account(self.__user_repository ,dto.get_account())
        self.__verify_password(user)
        user_dto = self.__enable_account_service.enable(EnableDto(user.get_id()))
        return user_dto
    
    def __verify_password(self, user: ClientUser, password: str) -> None:
        if not user.verify_password(password):
            raise IncorrectPasswordException.incorrect_password(password)