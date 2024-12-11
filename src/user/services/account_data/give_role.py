from src.user.data_providers import SaveUser
from src.user.domain import UserAccount
from .abstract_give_role import IGiveRole
from ..dto import GiveRoleDto, UserAccountDto
from ..user_is_registered import UserIsRegistered
from ..role_is_registered import RoleIsRegistered
from ..user_account_mapper import UserAccountMapper
from typing import List

class GiveRole(IGiveRole):
    def __init__(self, save_user: SaveUser,
                 user_is_registered: UserIsRegistered,
                 role_is_registered: RoleIsRegistered) -> None:
        self.__save_user = save_user
        self.__user_is_registered = user_is_registered
        self.__role_is_registered = role_is_registered
        self.__mapper = UserAccountMapper()
    
    def give(self, dto: GiveRoleDto) -> UserAccountDto:
        user = self.__user_is_registered.is_registered_by_id(dto.get_id())
        user = self.__give_role(user, dto.get_roles())
        return self.__mapper.to_dto(user)
    
    def __give_role(self, user: UserAccount, roles: List[str]) -> UserAccount:
        _roles = self.__role_is_registered.verify_is_all_registered(roles)
        user.add_roles(_roles)
        return self.__save_user.save(user)