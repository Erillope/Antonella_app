from ...domain import Role
from ...data_providers import RoleRepository
from ..dto import RoleDto, AddRoleDto
from ..role_is_registered import RoleIsRegistered
from .IAdd_role import IAddRole
from singleton_decorator import singleton

@singleton
class AddRole(IAddRole):
    def __init__(self, role_repository: RoleRepository) -> None:
        self.__role_repository = role_repository
    
    def add(self, dto: AddRoleDto) -> RoleDto:
        RoleIsRegistered.is_registered(self.__role_repository, dto.get_role())
        role = self.__role_repository.save(Role(dto.get_role()))
        return RoleDto.generate_dto(role)