from src.user.account.data_providers import GetUser, UserNotFoundException, ExistsUser
from src.user.employee_user.domain import EmployeeUser
from .employee_user_table_data import EmployeeUserTableData
from .employee_user_table_mapper import EmployeeUserTableMapper
from typing import List
from singleton_decorator import singleton

@singleton
class DjangoGetEmployeeUser(GetUser):
    def __init__(self, exists_employee_user: ExistsUser) -> None:
        super().__init__()
        self.__mapper = EmployeeUserTableMapper()
        self.__exists_employee_user = exists_employee_user
        
    def get_all(self) -> List[EmployeeUser]:
        employee_tables = EmployeeUserTableData.objects.all()
        employees = [self.__mapper.to_employee_user(table) for table in employee_tables]
        return employees
    
    def get_by_account(self, account: str) -> EmployeeUser:
        if self.__exists_employee_user.exists_by_account(account):
            employee_table = EmployeeUserTableData.objects.get(account=account)
            employee = self.__mapper.to_employee_user(employee_table)
            return employee
        else:
            raise UserNotFoundException.not_found(account)
    
    def get_by_id(self, id: str) -> EmployeeUser:
        if self.__exists_employee_user.exists_by_id(id):
            employee_table = EmployeeUserTableData.objects.get(id=id)
            employee = self.__mapper.to_employee_user(employee_table)
            return employee
        else:
            raise UserNotFoundException.not_found(id)