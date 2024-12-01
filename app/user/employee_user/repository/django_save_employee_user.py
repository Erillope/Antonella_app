from src.user.account.data_providers import SaveUser
from src.user.employee_user.domain import EmployeeUser, Role
from .employee_user_table_data import EmployeeUserTableData
from .user_role_table_data import UserRoleTableData
from .employee_user_table_mapper import EmployeeUserTableMapper
from typing import Set
from singleton_decorator import singleton

@singleton
class DjangoSaveEmployee(SaveUser):
    def __init__(self) -> None:
        super().__init__()
        self.__mapper = EmployeeUserTableMapper()

    def save(self, employee: EmployeeUser) -> EmployeeUser:
        employee_table = self.__mapper.to_employee_table(employee)
        employee_table.save()
        self.__save_roles(employee, employee_table)
        saved_employee = self.__mapper.to_employee_user(employee_table)
        return saved_employee
    
    def __save_roles(self, employee: EmployeeUser, employee_table: EmployeeUserTableData) -> None:
        user_role_tables = UserRoleTableData.objects.filter(employee=employee_table)
        if self.__table_have_more_role_than_employee(employee, user_role_tables):
            self.__take_roles(user_role_tables, employee)
        if self.__employee_have_more_role_than_table(employee, user_role_tables):
            self.__give_role(employee, employee_table)
            
    def __table_have_more_role_than_employee(self, employee: EmployeeUser,
                                             user_role_tables: Set[UserRoleTableData]) -> bool:
        return len(user_role_tables) > len(employee.get_roles())
    
    def __employee_have_more_role_than_table(self, employee: EmployeeUser,
                                             user_role_tables: Set[UserRoleTableData]) -> bool:
        return len(user_role_tables) < len(employee.get_roles())
    
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