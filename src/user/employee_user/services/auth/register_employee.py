from src.user.account.data_providers import SaveUser
from src.user.account.services.user_is_registered import UserIsRegistered
from ...domain import EmployeeUser
from ..dto import RegisterEmployeeDto, EmployeeUserDto, GiveRoleDto
from ..account_data import IGiveRole
from ..role_is_registered import RoleIsRegistered
from ..employee_user_mapper import EmployeeUserMapper
from .IRegister_employee import IRegisterEmployee
from singleton_decorator import singleton

@singleton
class RegisterEmployee(IRegisterEmployee):
    def __init__(self, save_employee: SaveUser,
                 give_role_service: IGiveRole,
                 employee_is_registered: UserIsRegistered,
                 role_is_registered: RoleIsRegistered) -> None:
        self.__save_employee = save_employee
        self.__give_role_service = give_role_service
        self.__employee_is_registered = employee_is_registered
        self.__role_is_registered = role_is_registered
        self.__mapper = EmployeeUserMapper()
    
    def register_employee(self, dto: RegisterEmployeeDto) -> EmployeeUserDto:
        self.__verify(dto)
        employee = self.__register(dto)
        employee_dto = self.__give_role_service.give(GiveRoleDto(employee.get_id(), dto.get_roles()))
        return employee_dto
    
    def __verify(self, dto: RegisterEmployeeDto) -> None:
        self.__employee_is_registered.verify_is_already_registered(dto.get_account())
        self.__role_is_registered.verify_is_all_registered(dto.get_roles())
        
    def __register(self, dto: RegisterEmployeeDto) -> EmployeeUser:
        employee = self.__mapper.to_user(dto)
        return self.__save_employee.save(employee)