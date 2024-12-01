from src.user.account import UserAccount
from ...data_providers import SaveUser
from ..user_is_registered import UserIsRegistered
from ..dto import SignUpDto, UserAccountDto
from .ISign_up import ISignUp
from ..user_account_mapper import UserAccountMapper

class SignUp(ISignUp):
    def __init__(self, save_user: SaveUser, user_is_registered: UserIsRegistered, 
                 mapper: UserAccountMapper) -> None:
        self.__user_is_registered = user_is_registered
        self.__save_user = save_user
        self.__mapper = mapper
        
    def sign_up(self, dto: SignUpDto) -> UserAccountDto:
        self.__user_is_registered.verify_is_already_registered(dto.get_account())
        user = self.__register(dto)
        return self.__mapper.to_dto(user)
    
    def __register(self, dto: SignUpDto) -> UserAccount:
        user = self.__mapper.to_user(dto)
        return self.__save_user.save(user)