from src.user.data_providers import SaveUser, GetUser
from src.user.domain import UserAccount
from ..dto import UserAccountDto, EnableDto
from ..mapper import UserAccountMapper
from .abstract_enable_user_account import IEnableUserAccount

class EnableUserAccount(IEnableUserAccount):
    def __init__(self, save_user: SaveUser, get_user: GetUser) -> None:
        self.__get_user = get_user
        self.__save_user = save_user
        self.__mapper = UserAccountMapper()
        
    def enable(self, dto: EnableDto) -> UserAccountDto:
        user = self.__get_user.get_by_id(dto.get_id())
        user = self.__enable_account(user)
        roles = self.__get_user.get_roles(user.get_id())
        return self.__mapper.to_dto(user, roles)
    
    def __enable_account(self, user: UserAccount) -> UserAccount:
        if not user.is_enable():
            user.enable()
            return self.__save_user.save(user)
        return user