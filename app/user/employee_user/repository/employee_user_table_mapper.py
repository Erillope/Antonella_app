from src.user.employee_user.domain import EmployeeUser, Role, EmployeeUserFactory
from src.user.account import AccountStatus
from .employee_user_table_data import EmployeeUserTableData
from .user_role_table_data import UserRoleTableData
from .role_table_data import RoleTableData
from singleton_decorator import singleton

@singleton
class EmployeeUserTableMapper:
    def to_employee_table(self, employee: EmployeeUser) -> EmployeeUserTableData:
        return EmployeeUserTableData(
            id = employee.get_id(),
            account = employee.get_account(),
            name = employee.get_name(),
            password = employee.get_password(),
            status = employee.get_status().value,
            joined_date = employee.get_joined_date()
        )
    
    def to_employee_user(self, employee_table: EmployeeUserTableData) -> EmployeeUser:
        return EmployeeUserFactory.create(
            id = str(employee_table.id),
            account = employee_table.account,
            name = employee_table.name,
            password = employee_table.password,
            roles = set([table.role for table in UserRoleTableData.get_roles_from_employee(employee_table)]),
            status = AccountStatus(employee_table.status),
            joined_date = employee_table.joined_date
            )
        
    def to_role_table(self, role: Role) -> RoleTableData:
        return RoleTableData(role.get_value())
    
    def to_role(self, role_table: RoleTableData) -> Role:
        return Role(role_table.role)