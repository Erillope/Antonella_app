from ...data_providers import EmployeeUserRepository, RoleRepository
from ...domain import EmployeeUser
from ..dto import GiveRoleDto, EmployeeUserDto
from ..employee_is_registered import EmployeeIsRegistered
from ..role_is_registered import RoleIsRegistered
from .IGive_role import IGiveRole
from singleton_decorator import singleton
from typing import Set

@singleton
class GiveRole(IGiveRole):
    def __init__(self, employee_repository: EmployeeUserRepository, role_repository: RoleRepository) -> None:
        self.__employee_repository = employee_repository
        self.__role_repository = role_repository
    
    def give(self, dto: GiveRoleDto) -> EmployeeUserDto:
        employee = EmployeeIsRegistered.is_registered_by_id(self.__employee_repository, dto.get_id())
        employee = self.__give_role(employee, dto.get_roles())
        return EmployeeUserDto.generate_dto(employee)
    
    def __give_role(self, employee: EmployeeUser, roles: Set[str]) -> EmployeeUser:
        RoleIsRegistered.verify_is_all_registered(self.__role_repository, roles)
        employee.add_roles(roles)
        return self.__employee_repository.save(employee)