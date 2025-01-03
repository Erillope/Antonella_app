from src.user import data_providers
from ..dto import RoleDto, DeleteRoleDto
from ..mapper import RoleMapper
from .abstract_delete_role import IDeleteRole

class DeleteRole(IDeleteRole):
    def __init__(self, delete_role: data_providers.DeleteRole) -> None:
        self.__delete_role = delete_role
        self.__mapper = RoleMapper()
    
    def delete(self, dto: DeleteRoleDto) -> RoleDto:
        role = self.__delete_role.delete_by_name(dto.get_role())
        return self.__mapper.to_dto(role)