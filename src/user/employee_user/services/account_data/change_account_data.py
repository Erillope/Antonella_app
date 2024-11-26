from ...data_providers import EmployeeUserRepository
from ...domain import EmployeeUser
from ..dto import ChangeDataDto, EmployeeUserDto
from ..employee_is_registered import EmployeeIsRegistered
from .IChange_account_data import IChangeAccountData
from singleton_decorator import singleton

@singleton
class ChangeAccountData(IChangeAccountData):
    def __init__(self, employee_repository: EmployeeUserRepository) -> None:
        self.__employee_repository = employee_repository
        
    def change_data(self, dto: ChangeDataDto) -> EmployeeUserDto:
        employee = EmployeeIsRegistered.is_registered_by_id(self.__employee_repository, dto.get_id())
        employee = self.__change(employee, dto)
        return EmployeeUserDto.generate_dto(employee)
        
    def __change(self, employee: EmployeeUser, dto: ChangeDataDto) -> EmployeeUser:
        employee.change_account(dto.get_account())
        employee.change_name(dto.get_name())
        employee.change_password(dto.get_password())
        return self.__employee_repository.save(employee)