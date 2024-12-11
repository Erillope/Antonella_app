from src.user.data_providers import SaveRole
from .abstract_rename_role import IRenameRole
from ..dto import RenameRoleDto, RoleDto
from ..role_mapper import RoleMapper
from ..role_is_registered import RoleIsRegistered

class RenameRole(IRenameRole):
    def __init__(self, role_is_registered: RoleIsRegistered, save_role: SaveRole):
        self.__role_is_registered = role_is_registered
        self.__mapper = RoleMapper()
        self.__save_role = save_role
    
    def rename(self, dto: RenameRoleDto) -> RoleDto:
        self.__role_is_registered.verify_is_already_registered(dto.get_new_role())
        role = self.__role_is_registered.is_registered(dto.get_role())
        role.rename(dto.get_new_role())
        saved_role = self.__save_role.save(role)
        return self.__mapper.to_dto(saved_role)