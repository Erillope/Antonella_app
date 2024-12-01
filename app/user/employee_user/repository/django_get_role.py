from src.user.employee_user.data_providers import GetRole
from src.user.employee_user.domain import Role
from .role_table_data import RoleTableData
from .employee_user_table_mapper import EmployeeUserTableMapper
from typing import Set
from singleton_decorator import singleton

@singleton
class DjangoGetRole(GetRole):
    def __init__(self) -> None:
        super().__init__()
        self.__mapper = EmployeeUserTableMapper()
        
    def get_all(self) -> Set[Role]:
        role_tables = RoleTableData.objects.all()
        roles = [self.__mapper.to_role(role) for role in role_tables]
        return roles