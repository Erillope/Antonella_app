from ..data_providers import GetRole, SaveRole, DeleteRole, ExistsRole
from abc import ABC, abstractmethod

class RoleRepositoryConfiguration(ABC):
    @abstractmethod
    def construct_get_role(self) -> GetRole: ...
    
    @abstractmethod
    def construct_save_role(self) -> SaveRole: ...
    
    @abstractmethod
    def construct_delete_role(self) -> DeleteRole: ...
    
    @abstractmethod
    def construct_exists_role(self) -> ExistsRole: ...