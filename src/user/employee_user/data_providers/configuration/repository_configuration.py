from src.user.account.data_providers import UserRepositoryConfiguration
from ..repository import GetRole, SaveRole, DeleteRole
from abc import ABC, abstractmethod

class EmployeeUserRepositoryConfiguration(UserRepositoryConfiguration):    
    @abstractmethod
    def construct_get_role(self) -> GetRole: ...
    
    @abstractmethod
    def construct_save_role(self) -> SaveRole: ...
    
    @abstractmethod
    def construct_delete_role(self) -> DeleteRole: ...