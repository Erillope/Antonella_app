from src.common.repository import SaveModel
from src.user.data_providers import GetRole, ExistsRole
from src.user.domain import Role
from .abstract_rename_role import IRenameRole
from ..dto import RenameRoleDto, RoleDto
from ..exception import RoleIsAlreadyRegisteredException
from ..mapper import RoleMapper

class RenameRole(IRenameRole):
    def __init__(self, exists_role: ExistsRole, save_role: SaveModel[Role], get_role: GetRole) -> None:
        self.__exists_role = exists_role
        self.__get_role = get_role
        self.__mapper = RoleMapper()
        self.__save_role = save_role
    
    def rename(self, dto: RenameRoleDto) -> RoleDto:
        self.__verify_is_already_exists(dto.get_new_role())
        role = self.__get_role.get_by_name(dto.get_role())
        role.rename(dto.get_new_role())
        saved_role = self.__save_role.save(role)
        return self.__mapper.to_dto(saved_role)
    
    def __verify_is_already_exists(self, role: str) -> None:
        if self.__exists_role.exists_by_name(role):
            raise RoleIsAlreadyRegisteredException.is_already_registered(role)