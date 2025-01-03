from src.user.data_providers import SaveUser, GetRole, GetUser
from .abstract_remove_role import IRemoveRole
from ..dto import UserAccountDto, RemoveRoleDto
from ..mapper import UserAccountMapper

class RemoveRole(IRemoveRole):
    def __init__(self, save_user: SaveUser, get_role: GetRole, get_user: GetUser) -> None:
        self.__save_user = save_user
        self.__get_role = get_role
        self.__get_user = get_user
        self.__mapper = UserAccountMapper()
    
    def remove(self, dto: RemoveRoleDto) -> UserAccountDto:
        roles = [self.__get_role.get_by_name(role) for role in dto.get_roles()]
        user = self.__save_user.remove_roles(dto.get_id(), roles)
        user_roles = self.__get_user.get_roles(user.get_id())
        return self.__mapper.to_dto(user, user_roles)