from src.user.employee_user.data_providers import (EmployeeUserRepositoryConfiguration,
                                                   EmployeeUserRepository, RoleRepository)
from ..repository import DjangoEmployeeUserRepository, DjangoRoleRepository
from singleton_decorator import singleton

@singleton
class DjangoEmployeeUserRepositoryConfiguration(EmployeeUserRepositoryConfiguration):
    def construct_employee_repository(self) -> EmployeeUserRepository:
        return DjangoEmployeeUserRepository()
    
    def construct_role_repository(self) -> RoleRepository:
        return DjangoRoleRepository()