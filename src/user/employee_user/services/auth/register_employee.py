from ...domain import EmployeeUserFactory, EmployeeUser
from ...data_providers import EmployeeUserRepository, RoleRepository
from ..dto import RegisterEmployeeDto, EmployeeUserDto, GiveRoleDto
from ..employee_is_registered import EmployeeIsRegistered
from ..account_data import IGiveRole
from ..role_is_registered import RoleIsRegistered
from .IRegister_employee import IRegisterEmployee
from singleton_decorator import singleton

@singleton
class RegisterEmployee(IRegisterEmployee):
    def __init__(self, employee_repository: EmployeeUserRepository, role_repository: RoleRepository,
                 give_role_service: IGiveRole) -> None:
        self.__employee_repository = employee_repository
        self.__role_repository = role_repository
        self.__give_role_service = give_role_service
    
    def register_employee(self, dto: RegisterEmployeeDto) -> EmployeeUserDto:
        EmployeeIsRegistered.verify_is_already_registered(self.__employee_repository, dto.get_account())
        RoleIsRegistered.verify_is_all_registered(self.__role_repository, dto.get_roles())
        employee = self.__register(dto)
        employee_dto = self.__give_role_service.give(GiveRoleDto(employee.get_id(), dto.get_roles()))
        return employee_dto
    
    def __register(self, dto: RegisterEmployeeDto) -> EmployeeUser:
        employee = EmployeeUserFactory.create_default(dto.get_account(), dto.get_name())
        return self.__employee_repository.save(employee)
        