from src.user.account.data_providers import UserAccountRepository
from src.user.employee_user.data_providers import EmployeeUserRepositoryConfiguration, RoleRepository
from ..repository import DjangoEmployeeUserRepository, DjangoRoleRepository
from singleton_decorator import singleton

@singleton
class DjangoEmployeeUserRepositoryConfiguration(EmployeeUserRepositoryConfiguration):
    def construct_employee_repository(self) -> UserAccountRepository:
        return DjangoEmployeeUserRepository()
    
    def construct_role_repository(self) -> RoleRepository:
        return DjangoRoleRepository()