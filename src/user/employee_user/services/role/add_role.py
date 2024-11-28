from ...domain import Role
from ...data_providers import RoleRepository
from ..dto import RoleDto, AddRoleDto
from ..role_is_registered import RoleIsRegistered
from ..employee_user_mapper import EmployeeUserMapper
from .IAdd_role import IAddRole
from singleton_decorator import singleton

@singleton
class AddRole(IAddRole):
    def __init__(self, role_repository: RoleRepository) -> None:
        self.__role_repository = role_repository
        self.__mapper = EmployeeUserMapper()
    
    def add(self, dto: AddRoleDto) -> RoleDto:
        RoleIsRegistered.is_registered(self.__role_repository, dto.get_role())
        role = self.__role_repository.save(Role(dto.get_role()))
        return self.__mapper.to_role_dto(role)