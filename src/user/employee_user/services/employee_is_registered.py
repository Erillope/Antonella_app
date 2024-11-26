from ..domain import EmployeeUser
from ..data_providers import EmployeeUserRepository
from .exception import EmployeeIsAlreadyRegisteredException, EmployeeIsNotRegisteredException

class EmployeeIsRegistered:
    @staticmethod
    def is_registered_by_account(employee_repository: EmployeeUserRepository, account: str) -> EmployeeUser:
        if employee_repository.exists_by_account(account):
            return employee_repository.get_by_account(account)
        raise EmployeeIsNotRegisteredException.is_not_registered(account)
    
    @staticmethod
    def is_registered_by_id(employee_repository: EmployeeUserRepository, id: str) -> EmployeeUser:
        if employee_repository.exists_by_id(id):
            return employee_repository.get_by_id(id)
        raise EmployeeIsNotRegisteredException.is_not_registered(id)
    
    @staticmethod
    def verify_is_already_registered(employee_repository: EmployeeUserRepository, account: str) -> EmployeeUser:
        if employee_repository.exists_by_account(account):
            raise EmployeeIsAlreadyRegisteredException.is_already_registered(account)