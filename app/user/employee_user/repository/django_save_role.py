from src.user.employee_user.data_providers import SaveRole
from src.user.employee_user.domain import Role
from .employee_user_table_mapper import EmployeeUserTableMapper
from singleton_decorator import singleton

@singleton
class DjangoSaveRole(SaveRole):
    def __init__(self) -> None:
        super().__init__()
        self.__mapper = EmployeeUserTableMapper()
    
    def save(self, role: Role) -> Role:
        role_table = self.__mapper.to_role_table(role)
        role_table.save()
        role = self.__mapper.to_role(role_table)
        return role