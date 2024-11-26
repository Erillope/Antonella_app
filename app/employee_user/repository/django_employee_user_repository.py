from src.user.employee_user.data_providers import EmployeeUserRepository, EmployeeUserNotFoundException
from src.user.employee_user.domain import EmployeeUser, Role
from .employee_user_table_data import EmployeeUserTableData
from .user_role_table_data import UserRoleTableData
from .employee_user_table_adapter import EmployeeUserTableAdapter
from typing import List, Set
from singleton_decorator import singleton

@singleton
class DjangoEmployeeUserRepository(EmployeeUserRepository):
    def get_all(self) -> List[EmployeeUser]:
        employee_tables = EmployeeUserTableData.objects.all()
        employees = [EmployeeUserTableAdapter.to_employee_user(table) for table in employee_tables]
        return employees
    
    def get_by_account(self, account: str) -> EmployeeUser:
        if self.exists_by_account(account):
            employee_table = EmployeeUserTableData.objects.get(account=account)
            employee = EmployeeUserTableAdapter.to_employee_user(employee_table)
            return employee
        else:
            raise EmployeeUserNotFoundException.not_found(account)
    
    def get_by_id(self, id: str) -> EmployeeUser:
        if self.exists_by_id(id):
            employee_table = EmployeeUserTableData.objects.get(id=id)
            employee = EmployeeUserTableAdapter.to_employee_user(employee_table)
            return employee
        else:
            raise EmployeeUserNotFoundException.not_found(id)
    
    def save(self, employee: EmployeeUser) -> EmployeeUser:
        employee_table = EmployeeUserTableAdapter.to_employee_user_table(employee)
        employee_table.save()
        user_role_tables = UserRoleTableData.objects.filter(employee=employee_table)
        if len(user_role_tables) > len(employee.get_roles()):
            self.__take_roles(user_role_tables, employee)
        if len(user_role_tables) < len(employee.get_roles()):
            self.__give_role(employee, employee_table)
        saved_employee = EmployeeUserTableAdapter.to_employee_user(employee_table)
        return saved_employee
    
    def __take_roles(self, user_role_tables: Set[UserRoleTableData], employee: EmployeeUser) -> None:
        for user_role in user_role_tables:
            role = EmployeeUserTableAdapter.to_role(user_role.role)
            if not employee.have_role(role.get_value()):
                user_role.delete()
    
    def __give_role(self,employee: EmployeeUser, employee_table: EmployeeUserTableData) -> None:
        for role in employee.get_roles():
            role_table = EmployeeUserTableAdapter.to_role_table(Role(role))
            if not UserRoleTableData.objects.filter(employee=employee_table, role=role_table).exists():
                UserRoleTableData.objects.create(employee=employee_table, role=role_table)
                
    def exists_by_account(self, account: str) -> bool:
        return EmployeeUserTableData.objects.filter(account=account).exists()
    
    def exists_by_id(self, id: str) -> bool:
        return EmployeeUserTableData.objects.filter(id=id).exists()