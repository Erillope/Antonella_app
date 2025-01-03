from src.user.data_providers import SaveUser, GetUser
from src.user.domain import UserAccount
from ..dto import UserAccountDto, DisableDto
from ..mapper import UserAccountMapper
from .abstract_disable_user_account import IDisableUserAccount

class DisableUserAccount(IDisableUserAccount):
    def __init__(self, save_user: SaveUser, get_user: GetUser) -> None:
        self.__get_user = get_user
        self.__save_user = save_user
        self.__mapper = UserAccountMapper()
        
    def disable(self, dto: DisableDto) -> UserAccountDto:
        user = self.__get_user.get_by_id(dto.get_id())
        user = self.__disable_account(user)
        roles = self.__get_user.get_roles(user.get_id())
        return self.__mapper.to_dto(user, roles)
    
    def __disable_account(self, user: UserAccount) -> UserAccount:
        if user.is_enable():
            user.disable()
            return self.__save_user.save(user)
        return user
        