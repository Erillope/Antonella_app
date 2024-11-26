from ...data_providers import EmployeeUserRepository
from ...domain import EmployeeUser
from ..dto import EnableDto, EmployeeUserDto
from ..employee_is_registered import EmployeeIsRegistered
from .IEnable_employee_user_account import IEnableEmployeeUserAccount
from singleton_decorator import singleton

@singleton
class EnableEmployeeUserAccount(IEnableEmployeeUserAccount):
    def __init__(self, employee_repository: EmployeeUserRepository) -> None:
        self.__employee_repository = employee_repository
        
    def enable(self, dto: EnableDto) -> EmployeeUserDto:
        employee = EmployeeIsRegistered.is_registered_by_id(self.__employee_repository, dto.get_id())
        employee = self.__enable_account(employee)
        return EmployeeUserDto.generate_dto(employee)
    
    def __enable_account(self, employee: EmployeeUser) -> EmployeeUser:
        if not employee.is_enable():
            employee.enable()
            return self.__employee_repository.save(employee)
        return employee