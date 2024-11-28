from ...domain import Role
from ...data_providers import RoleRepository
from ..dto import RoleDto, RemoveRoleDto
from ..role_is_registered import RoleIsRegistered
from ..employee_user_mapper import EmployeeUserMapper
from .IRemove_role import IRemoveRole
from singleton_decorator import singleton

@singleton
class RemoveRole(IRemoveRole):
    def __init__(self, role_repository: RoleRepository) -> None:
        self.__role_repository = role_repository
        self.__mapper = EmployeeUserMapper()
    
    def remove(self, dto: RemoveRoleDto) -> RoleDto:
        RoleIsRegistered.is_not_registered(self.__role_repository, dto.get_role())
        role = self.__role_repository.remove(Role(dto.get_role()))
        return self.__mapper.to_role_dto(role)