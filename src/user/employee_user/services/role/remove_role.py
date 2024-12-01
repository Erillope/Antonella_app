from ...domain import Role
from ...data_providers import DeleteRole
from ..role_is_registered import RoleIsRegistered
from ..dto import RoleDto, RemoveRoleDto
from ..employee_user_mapper import EmployeeUserMapper
from .IRemove_role import IRemoveRole
from singleton_decorator import singleton

@singleton
class RemoveRole(IRemoveRole):
    def __init__(self, delete_role: DeleteRole, role_is_registered: RoleIsRegistered) -> None:
        self.__delete_role = delete_role
        self.__role_is_registered = role_is_registered
        self.__mapper = EmployeeUserMapper()
    
    def remove(self, dto: RemoveRoleDto) -> RoleDto:
        self.__role_is_registered.is_not_registered(dto.get_role())
        role = self.__delete_role.delete(Role(dto.get_role()))
        return self.__mapper.to_role_dto(role)