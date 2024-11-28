from src.user.account.services.user_is_registered import UserIsRegistered
from src.user.account.data_providers import UserAccountRepository
from ...data_providers import RoleRepository
from ...domain import EmployeeUser
from ..dto import GiveRoleDto, EmployeeUserDto
from ..role_is_registered import RoleIsRegistered
from ..employee_user_mapper import EmployeeUserMapper
from .IGive_role import IGiveRole
from singleton_decorator import singleton
from typing import Set

@singleton
class GiveRole(IGiveRole):
    def __init__(self, employee_repository: UserAccountRepository, role_repository: RoleRepository) -> None:
        self.__employee_repository = employee_repository
        self.__role_repository = role_repository
        self.__mapper = EmployeeUserMapper()
    
    def give(self, dto: GiveRoleDto) -> EmployeeUserDto:
        employee = UserIsRegistered.is_registered_by_id(self.__employee_repository, dto.get_id())
        employee = self.__give_role(employee, dto.get_roles())
        return self.__mapper.to_dto(employee)
    
    def __give_role(self, employee: EmployeeUser, roles: Set[str]) -> EmployeeUser:
        RoleIsRegistered.verify_is_all_registered(self.__role_repository, roles)
        employee.add_roles(roles)
        return self.__employee_repository.save(employee)