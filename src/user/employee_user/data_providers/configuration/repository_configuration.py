from src.user.account.data_providers import UserAccountRepository
from ..repository import RoleRepository
from abc import ABC, abstractmethod

class EmployeeUserRepositoryConfiguration(ABC):
    @abstractmethod
    def construct_employee_repository(self) -> UserAccountRepository: ...
    
    @abstractmethod
    def construct_role_repository(self) -> RoleRepository: ...