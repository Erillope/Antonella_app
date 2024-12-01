from ...data_providers import SaveUser
from ...domain import UserAccount
from ..dto import EnableDto, UserAccountDto
from ..user_is_registered import UserIsRegistered
from ..user_account_mapper import UserAccountMapper
from .IEnable_user_account import IEnableUserAccount

class EnableUserAccount(IEnableUserAccount):
    def __init__(self, save_user: SaveUser, user_is_registered: UserIsRegistered, 
                 mapper: UserAccountMapper) -> None:
        self.__user_is_registered = user_is_registered
        self.__save_user = save_user
        self.__mapper = mapper
        
    def enable(self, dto: EnableDto) -> UserAccountDto:
        user = self.__user_is_registered.is_registered_by_id(dto.get_id())
        user = self.__enable_account(user)
        return self.__mapper.to_dto(user)
    
    def __enable_account(self, user: UserAccount) -> UserAccount:
        if not user.is_enable():
            user.enable()
            return self.__save_user.save(user)
        return user