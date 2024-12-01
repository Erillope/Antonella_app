from src.user.account.services.user_is_registered import UserIsRegistered
from src.user.account.data_providers import SaveUser
from ...domain import EmployeeUser
from ..dto import GiveRoleDto, EmployeeUserDto
from ..role_is_registered import RoleIsRegistered
from ..employee_user_mapper import EmployeeUserMapper
from .IGive_role import IGiveRole
from singleton_decorator import singleton
from typing import Set

@singleton
class GiveRole(IGiveRole):
    def __init__(self, save_employee: SaveUser,
                 employee_is_registered: UserIsRegistered,
                 role_is_registered: RoleIsRegistered) -> None:
        self.__save_employee = save_employee
        self.__employee_is_registered = employee_is_registered
        self.__role_is_registered = role_is_registered
        self.__mapper = EmployeeUserMapper()
    
    def give(self, dto: GiveRoleDto) -> EmployeeUserDto:
        employee = self.__employee_is_registered.is_registered_by_id(dto.get_id())
        employee = self.__give_role(employee, dto.get_roles())
        return self.__mapper.to_dto(employee)
    
    def __give_role(self, employee: EmployeeUser, roles: Set[str]) -> EmployeeUser:
        self.__role_is_registered.verify_is_all_registered(roles)
        employee.add_roles(roles)
        return self.__save_employee.save(employee)