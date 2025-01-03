from src.common.repository import ExistsModel, SaveModel
from src.user.domain import Role
from ..data_providers import GetRole, DeleteRole
from abc import ABC, abstractmethod

class RoleRepositoryConfiguration(ABC):
    @abstractmethod
    def construct_get_role(self) -> GetRole: ...
    
    @abstractmethod
    def construct_save_role(self) -> SaveModel[Role]: ...
    
    @abstractmethod
    def construct_delete_role(self) -> DeleteRole: ...
    
    @abstractmethod
    def construct_exists_role(self) -> ExistsModel: ...