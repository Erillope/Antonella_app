from src.user.domain import UserAccount
from src.user.data_providers import GetUser
from ..account_data import IEnableUserAccount
from ..exception import IncorrectPasswordException
from ..dto import UserAccountDto, EnableDto, SignInDto
from .abstract_sign_in import ISignIn

class SignIn(ISignIn):
    def __init__(self, get_user: GetUser, enable_account_service: IEnableUserAccount) -> None:
        self.__get_user = get_user
        self.__enable_account_service = enable_account_service
        
    def sign_in(self, dto: SignInDto) -> UserAccountDto:
        user = self.__get_user.get_by_account(dto.get_account())
        self.__verify_password(user, dto.get_password())
        user_dto = self.__enable_account_service.enable(EnableDto(user.get_id()))
        return user_dto
    
    def __verify_password(self, user: UserAccount, password: str) -> None:
        if not user.verify_password(password):
            raise IncorrectPasswordException.incorrect_password(password)