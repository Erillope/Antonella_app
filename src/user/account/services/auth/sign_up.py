from src.user.account import UserAccount
from ...data_providers import UserAccountRepository
from ..user_is_registered import UserIsRegistered
from ..dto import SignUpDto, UserAccountDto
from .ISign_up import ISignUp
from ..user_account_mapper import UserAccountMapper
from singleton_decorator import singleton

class SignUp(ISignUp):
    def __init__(self, user_repository: UserAccountRepository, mapper: UserAccountMapper) -> None:
        self.__user_repository = user_repository
        self.__mapper = mapper
        
    def sign_up(self, dto: SignUpDto) -> UserAccountDto:
        UserIsRegistered.verify_is_already_registered(self.__user_repository, dto.get_account())
        user = self.__register(dto)
        return self.__mapper.to_dto(user)
    
    def __register(self, dto: SignUpDto) -> UserAccount:
        user = self.__mapper.to_user(dto)
        return self.__user_repository.save(user)