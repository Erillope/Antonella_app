from ...domain import Role
from ...data_providers import SaveRole
from ..role_is_registered import RoleIsRegistered
from ..dto import RoleDto, AddRoleDto
from ..employee_user_mapper import EmployeeUserMapper
from .IAdd_role import IAddRole
from singleton_decorator import singleton

@singleton
class AddRole(IAddRole):
    def __init__(self, save_role: SaveRole, role_is_registered: RoleIsRegistered) -> None:
        self.__save_role = save_role
        self.__role_is_registered = role_is_registered
        self.__mapper = EmployeeUserMapper()
    
    def add(self, dto: AddRoleDto) -> RoleDto:
        self.__role_is_registered.is_registered(dto.get_role())
        role = self.__save_role.save(Role(dto.get_role()))
        return self.__mapper.to_role_dto(role)