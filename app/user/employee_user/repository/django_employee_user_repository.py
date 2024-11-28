from src.user.account.data_providers import UserAccountRepository, UserNotFoundException
from app.user.account.user_account_table_data import UserAccountTableData
from src.user.employee_user.domain import EmployeeUser, Role
from .employee_user_table_data import EmployeeUserTableData
from .user_role_table_data import UserRoleTableData
from .employee_user_table_mapper import EmployeeUserTableMapper
from typing import List, Set
from singleton_decorator import singleton

@singleton
class DjangoEmployeeUserRepository(UserAccountRepository):
    def __init__(self) -> None:
        super().__init__()
        self.__mapper = EmployeeUserTableMapper()
        
    def get_all(self) -> List[EmployeeUser]:
        employee_tables = EmployeeUserTableData.objects.all()
        employees = [self.__mapper.to_employee_user(table) for table in employee_tables]
        return employees
    
    def get_by_account(self, account: str) -> EmployeeUser:
        if self.exists_by_account(account):
            employee_table = EmployeeUserTableData.objects.get(account=account)
            employee = self.__mapper.to_employee_user(employee_table)
            return employee
        else:
            raise UserNotFoundException.not_found(account)
    
    def get_by_id(self, id: str) -> EmployeeUser:
        if self.exists_by_id(id):
            employee_table = EmployeeUserTableData.objects.get(id=id)
            employee = self.__mapper.to_employee_user(employee_table)
            return employee
        else:
            raise UserNotFoundException.not_found(id)
    
    def save(self, employee: EmployeeUser) -> EmployeeUser:
        employee_table = self.__mapper.to_employee_table(employee)
        employee_table.save()
        user_role_tables = UserRoleTableData.objects.filter(employee=employee_table)
        if len(user_role_tables) > len(employee.get_roles()):
            self.__take_roles(user_role_tables, employee)
        if len(user_role_tables) < len(employee.get_roles()):
            self.__give_role(employee, employee_table)
        saved_employee = self.__mapper.to_employee_user(employee_table)
        return saved_employee
    
    def __take_roles(self, user_role_tables: Set[UserRoleTableData], employee: EmployeeUser) -> None:
        for user_role in user_role_tables:
            role = self.__mapper.to_role(user_role.role)
            if not employee.have_role(role.get_value()):
                user_role.delete()
    
    def __give_role(self,employee: EmployeeUser, employee_table: EmployeeUserTableData) -> None:
        for role in employee.get_roles():
            role_table = self.__mapper.to_role_table(Role(role))
            if not UserRoleTableData.objects.filter(employee=employee_table, role=role_table).exists():
                UserRoleTableData.objects.create(employee=employee_table, role=role_table)
                
    def exists_by_account(self, account: str) -> bool:
        return UserAccountTableData.objects.filter(account=account).exists()
    
    def exists_by_id(self, id: str) -> bool:
        return UserAccountTableData.objects.filter(id=id).exists()