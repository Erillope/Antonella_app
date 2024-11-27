from src.user.employee_user.data_providers import RoleRepository, RoleNotFoundException
from src.user.employee_user.domain import Role
from .role_table_data import RoleTableData
from .employee_user_table_adapter import EmployeeUserTableAdapter
from typing import Set
from singleton_decorator import singleton

@singleton
class DjangoRoleRepository(RoleRepository):
    def get_all(self) -> Set[Role]:
        role_tables = RoleTableData.objects.all()
        roles = [EmployeeUserTableAdapter.to_role(role) for role in role_tables]
        return roles
    
    def save(self, role: Role) -> Role:
        role_table = EmployeeUserTableAdapter.to_role_table(role)
        role_table.save()
        role = EmployeeUserTableAdapter.to_role(role_table)
        return role
    
    def remove(self, role: Role) -> Role:
        role_table = EmployeeUserTableAdapter.to_role_table(role)
        role = EmployeeUserTableAdapter.to_role(role_table)
        role_table.delete()
        return role
    
    def exists(self, role: str) -> bool:
        return RoleTableData.objects.filter(role=role).exists()