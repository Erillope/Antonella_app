from ..services import IAddRole, IDeleteRole, IRenameRole, IGetAllRoles, RoleIsRegistered
from abc import ABC, abstractmethod

class RoleServiceConfiguration(ABC):
    @abstractmethod
    def construct_role_is_registered_service(self) -> RoleIsRegistered: ...
    
    @abstractmethod
    def construct_add_role_service(self) -> IAddRole: ...
    
    @abstractmethod
    def construct_delete_role_service(self) -> IDeleteRole: ...
    
    @abstractmethod
    def construct_rename_role_service(self) -> IRenameRole: ...
    
    @abstractmethod
    def construct_get_all_roles_service(self) -> IGetAllRoles: ...