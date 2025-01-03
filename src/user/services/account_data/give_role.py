from src.user.data_providers import SaveUser, GetRole
from .abstract_give_role import IGiveRole
from ..dto import GiveRoleDto, UserAccountDto
from ..mapper import UserAccountMapper

class GiveRole(IGiveRole):
    def __init__(self, save_user: SaveUser, get_role: GetRole) -> None:
        self.__save_user = save_user
        self.__get_role = get_role
        self.__mapper = UserAccountMapper()
    
    def give(self, dto: GiveRoleDto) -> UserAccountDto:
        roles = [self.__get_role.get_by_name(role) for role in dto.get_roles()]
        user = self.__save_user.give_roles(dto.get_id(), roles)
        return self.__mapper.to_dto(user, roles)