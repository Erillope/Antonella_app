from ...data_providers import EmployeeUserRepository
from ...domain import EmployeeUser
from ..dto import DisableDto, EmployeeUserDto
from ..employee_is_registered import EmployeeIsRegistered
from .IDisable_employee_user_account import IDisableEmployeeUserAccount
from singleton_decorator import singleton

@singleton
class DisableEmployeeUserAccount(IDisableEmployeeUserAccount):
    def __init__(self, employee_repository: EmployeeUserRepository) -> None:
        self.__employee_repository = employee_repository
        
    def disable(self, dto: DisableDto) -> EmployeeUserDto:
        employee = EmployeeIsRegistered.is_registered_by_id(self.__employee_repository, dto.get_id())
        employee = self.__disable_account(employee)
        return EmployeeUserDto.generate_dto(employee)
    
    def __disable_account(self, employee: EmployeeUser) -> EmployeeUser:
        if employee.is_enable():
            employee.disable()
            return self.__employee_repository.save(employee)
        return employee