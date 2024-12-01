from src.user.employee_user.data_providers import DeleteRole
from src.user.employee_user.domain import Role
from .employee_user_table_mapper import EmployeeUserTableMapper
from typing import Set
from singleton_decorator import singleton

@singleton
class DjangoDeleteRole(DeleteRole):
    def __init__(self) -> None:
        super().__init__()
        self.__mapper = EmployeeUserTableMapper()
    
    def delete(self, role: Role) -> Role:
        role_table = self.__mapper.to_role_table(role)
        role = self.__mapper.to_role(role_table)
        role_table.delete()
        return role