from src.user.account.data_providers import UserAccountRepository
from src.user.account.services.user_is_registered import UserIsRegistered
from ...domain import EmployeeUser, EmployeeUserFactory
from ...data_providers import RoleRepository
from ..dto import RegisterEmployeeDto, EmployeeUserDto, GiveRoleDto
from ..account_data import IGiveRole
from ..role_is_registered import RoleIsRegistered
from ..employee_user_mapper import EmployeeUserMapper
from .IRegister_employee import IRegisterEmployee
from singleton_decorator import singleton

@singleton
class RegisterEmployee(IRegisterEmployee):
    def __init__(self, employee_repository: UserAccountRepository,role_repository: RoleRepository, give_role_service: IGiveRole) -> None:
        self.__employee_repository = employee_repository
        self.__role_repository = role_repository
        self.__give_role_service = give_role_service
        self.__mapper = EmployeeUserMapper()
    
    def register_employee(self, dto: RegisterEmployeeDto) -> EmployeeUserDto:
        UserIsRegistered.verify_is_already_registered(self.__employee_repository, dto.get_account())
        RoleIsRegistered.verify_is_all_registered(self.__role_repository, dto.get_roles())
        employee = self.__register(dto)
        employee_dto = self.__give_role_service.give(GiveRoleDto(employee.get_id(), dto.get_roles()))
        return employee_dto
    
    def __register(self, dto: RegisterEmployeeDto) -> EmployeeUser:
        employee = self.__mapper.to_user(dto)
        return self.__employee_repository.save(employee)