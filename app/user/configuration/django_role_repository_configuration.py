from src.user import RoleRepositoryConfiguration, GetRole, SaveRole, ExistsRole, DeleteRole
from ..repository import DjangoExistsRole, DjangoGetRole, DjangoSaveRole, DjangoDeleteRole

class DjangoRoleRepositoryConfiguration(RoleRepositoryConfiguration):
    def construct_delete_role(self) -> DeleteRole:
        return DjangoDeleteRole()
    
    def construct_exists_role(self) -> ExistsRole:
        return DjangoExistsRole()
    
    def construct_get_role(self) -> GetRole:
        return DjangoGetRole(
            exists_role = self.construct_exists_role()
        )
    
    def construct_save_role(self) -> SaveRole:
        return DjangoSaveRole()