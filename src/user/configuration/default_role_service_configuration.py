from ..services import IAddRole, IDeleteRole, IRenameRole, IGetAllRoles, RoleIsRegistered
from ..services.role import AddRole, DeleteRole, RenameRole, GetAllRoles
from .role_service_configuration import RoleServiceConfiguration
from .role_repository_configuration import RoleRepositoryConfiguration

class DefaultRoleServiceConfiguration(RoleServiceConfiguration):
    def __init__(self, role_repository_configuration: RoleRepositoryConfiguration) -> None:
        self.__role_repository_configuration = role_repository_configuration
    
    def construct_role_is_registered_service(self) -> RoleIsRegistered:
        return RoleIsRegistered(
            exists_role = self.__role_repository_configuration.construct_exists_role(),
            get_role = self.__role_repository_configuration.construct_get_role()
        )
    
    def construct_add_role_service(self) -> IAddRole:
        return AddRole(
            save_role = self.__role_repository_configuration.construct_save_role(),
            role_is_registered = self.construct_role_is_registered_service()
        )
    
    def construct_rename_role_service(self) -> IRenameRole:
        return RenameRole(
            role_is_registered = self.construct_role_is_registered_service(),
            save_role = self.__role_repository_configuration.construct_save_role()
        )
    
    def construct_delete_role_service(self) -> IDeleteRole:
        return DeleteRole(
            delete_role = self.__role_repository_configuration.construct_delete_role(),
            role_is_registered = self.construct_role_is_registered_service()
        )
    
    def construct_get_all_roles_service(self) -> IGetAllRoles:
        return GetAllRoles(
            get_role = self.__role_repository_configuration.construct_get_role()
        )