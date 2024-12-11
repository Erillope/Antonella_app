from src.user import data_providers
from ..role_is_registered import RoleIsRegistered
from ..dto import RoleDto, DeleteRoleDto
from ..role_mapper import RoleMapper
from .abstract_delete_role import IDeleteRole

class DeleteRole(IDeleteRole):
    def __init__(self, delete_role: data_providers.DeleteRole, role_is_registered: RoleIsRegistered) -> None:
        self.__delete_role = delete_role
        self.__role_is_registered = role_is_registered
        self.__mapper = RoleMapper()
    
    def delete(self, dto: DeleteRoleDto) -> RoleDto:
        role = self.__role_is_registered.is_registered(dto.get_role())
        role = self.__delete_role.delete(role)
        return self.__mapper.to_dto(role)