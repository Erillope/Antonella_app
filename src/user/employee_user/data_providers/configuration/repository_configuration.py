from ..repository import EmployeeUserRepository, RoleRepository
from abc import ABC, abstractmethod

class EmployeeUserRepositoryConfiguration(ABC):
    @abstractmethod
    def construct_employee_repository(self) -> EmployeeUserRepository: ...
    
    @abstractmethod
    def construct_role_repository(self) -> RoleRepository: ...