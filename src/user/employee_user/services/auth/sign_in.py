from ...data_providers import EmployeeUserRepository
from ...domain import EmployeeUser
from ..dto import SignInDto, EmployeeUserDto, EnableDto
from ..employee_is_registered import EmployeeIsRegistered
from ..account_data import IEnableEmployeeUserAccount
from ..exception import IncorrectPasswordException
from .ISign_in import ISingIn
from singleton_decorator import singleton

@singleton
class SignIn(ISingIn):
    def __init__(self, employee_repository: EmployeeUserRepository,
                 enable_account_service: IEnableEmployeeUserAccount) -> None:
        self.__employee_repository = employee_repository
        self.__enable_account_service = enable_account_service
        
    def sign_in(self, dto: SignInDto) -> EmployeeUserDto:
        employee = EmployeeIsRegistered.is_registered_by_account(self.__employee_repository ,dto.get_account())
        self.__verify_password(employee, dto.get_password())
        employee_dto = self.__enable_account_service.enable(EnableDto(employee.get_id()))
        return employee_dto
    
    def __verify_password(self, employee: EmployeeUser, password: str) -> None:
        if not employee.verify_password(password):
            raise IncorrectPasswordException.incorrect_password(password)