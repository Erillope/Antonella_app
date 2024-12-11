from src.user.domain import Role
from src.user.data_providers import SaveRole
from ..role_is_registered import RoleIsRegistered
from ..role_mapper import RoleMapper
from ..dto import RoleDto, AddRoleDto
from .abstract_add_role import IAddRole

class AddRole(IAddRole):
    def __init__(self, save_role: SaveRole, role_is_registered: RoleIsRegistered) -> None:
        self.__save_role = save_role
        self.__role_is_registered = role_is_registered
        self.__mapper = RoleMapper()
    
    def add(self, dto: AddRoleDto) -> RoleDto:
        self.__role_is_registered.verify_is_already_registered(dto.get_role())
        role = self.__mapper.to_role(dto.get_role())
        role = self.__save_role.save(role)
        return self.__mapper.to_dto(role)