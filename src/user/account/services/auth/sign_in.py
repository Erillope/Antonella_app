from ...data_providers import UserAccountRepository
from ...domain import UserAccount
from ..dto import SignInDto, UserAccountDto, EnableDto
from ..user_is_registered import UserIsRegistered
from ..account_data import IEnableUserAccount
from ..exception import IncorrectPasswordException
from .ISign_in import ISingIn

class SignIn(ISingIn):
    def __init__(self, user_repository: UserAccountRepository, enable_account_service: IEnableUserAccount) -> None:
        self.__user_repository = user_repository
        self.__enable_account_service = enable_account_service
        
    def sign_in(self, dto: SignInDto) -> UserAccountDto:
        user = UserIsRegistered.is_registered_by_account(self.__user_repository ,dto.get_account())
        self.__verify_password(user, dto.get_password())
        user_dto = self.__enable_account_service.enable(EnableDto(user.get_id()))
        return user_dto
    
    def __verify_password(self, user: UserAccount, password: str) -> None:
        if not user.verify_password(password):
            raise IncorrectPasswordException.incorrect_password(password)