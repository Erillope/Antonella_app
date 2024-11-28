from ...data_providers import UserAccountRepository
from ...domain import UserAccount
from ..dto import EnableDto, UserAccountDto
from ..user_is_registered import UserIsRegistered
from ..user_account_mapper import UserAccountMapper
from .IEnable_user_account import IEnableUserAccount

class EnableUserAccount(IEnableUserAccount):
    def __init__(self, user_repository: UserAccountRepository, mapper: UserAccountMapper) -> None:
        self.__user_repository = user_repository
        self.__mapper = mapper
        
    def enable(self, dto: EnableDto) -> UserAccountDto:
        user = UserIsRegistered.is_registered_by_id(self.__user_repository, dto.get_id())
        user = self.__enable_account(user)
        return self.__mapper.to_dto(user)
    
    def __enable_account(self, user: UserAccount) -> UserAccount:
        if not user.is_enable():
            user.enable()
            return self.__user_repository.save(user)
        return user