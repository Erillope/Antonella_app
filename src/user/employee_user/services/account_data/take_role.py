from ...data_providers import EmployeeUserRepository
from ...domain import EmployeeUser
from ..dto import TakeRoleDto, EmployeeUserDto
from ..employee_is_registered import EmployeeIsRegistered
from .ITake_role import ITakeRole
from singleton_decorator import singleton
from typing import Set

@singleton
class TakeRole(ITakeRole):
    def __init__(self, employee_repository: EmployeeUserRepository) -> None:
        self.__employee_repository = employee_repository
    
    def take(self, dto: TakeRoleDto) -> EmployeeUserDto:
        employee = EmployeeIsRegistered.is_registered_by_id(self.__employee_repository, dto.get_id())
        employee = self.__take_role(employee, dto.get_roles())
        return EmployeeUserDto.generate_dto(employee)
    
    def __take_role(self, employee: EmployeeUser, roles: Set[str]) -> EmployeeUser:
        employee.remove_roles(roles)
        return self.__employee_repository.save(employee)