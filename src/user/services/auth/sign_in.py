from src.user.domain import UserAccount
from ..dto import SignInDto, UserAccountDto, EnableDto
from ..user_is_registered import UserIsRegistered
from ..account_data import IEnableUserAccount
from ..exception import IncorrectPasswordException
from .abstract_sign_in import ISignIn

class SignIn(ISignIn):
    def __init__(self, user_is_registered: UserIsRegistered, enable_account_service: IEnableUserAccount) -> None:
        self.__user_is_registered = user_is_registered
        self.__enable_account_service = enable_account_service
        
    def sign_in(self, dto: SignInDto) -> UserAccountDto:
        user = self.__user_is_registered.is_registered_by_account(dto.get_account())
        self.__verify_password(user, dto.get_password())
        user_dto = self.__enable_account_service.enable(EnableDto(user.get_id()))
        return user_dto
    
    def __verify_password(self, user: UserAccount, password: str) -> None:
        if not user.verify_password(password):
            raise IncorrectPasswordException.incorrect_password(password)