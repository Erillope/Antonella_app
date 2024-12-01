from src.user.account.services.user_is_registered import UserIsRegistered
from src.user.account.data_providers import SaveUser
from ...domain import EmployeeUser
from ..dto import TakeRoleDto, EmployeeUserDto
from ..employee_user_mapper import EmployeeUserMapper
from .ITake_role import ITakeRole
from singleton_decorator import singleton
from typing import Set

@singleton
class TakeRole(ITakeRole):
    def __init__(self, save_employee: SaveUser, employee_is_registered: UserIsRegistered) -> None:
        self.__save_employee = save_employee
        self.__employee_is_registered = employee_is_registered
        self.__mapper = EmployeeUserMapper()
    
    def take(self, dto: TakeRoleDto) -> EmployeeUserDto:
        employee = self.__employee_is_registered.is_registered_by_id(dto.get_id())
        employee = self.__take_role(employee, dto.get_roles())
        return self.__mapper.to_dto(employee)
    
    def __take_role(self, employee: EmployeeUser, roles: Set[str]) -> EmployeeUser:
        employee.remove_roles(roles)
        return self.__save_employee.save(employee)