from src.common.repository import SaveModel
from src.user import RoleRepositoryConfiguration, GetRole, DeleteRole, Role, ExistsRole
from app.common.django_repository import DjangoSaveModel, DjangoExistsModel
from ..repository import DjangoGetRole, DjangoDeleteRole, RoleTableMapper, RoleTableData, DjangoExistsRole

class DjangoRoleRepositoryConfiguration(RoleRepositoryConfiguration):
    def construct_delete_role(self) -> DeleteRole:
        return DjangoDeleteRole()
    
    def construct_exists_role(self) -> ExistsRole:
        return DjangoExistsRole()
    
    def construct_get_role(self) -> GetRole:
        return DjangoGetRole()
    
    def construct_save_role(self) -> SaveModel[Role]:
        return DjangoSaveModel[RoleTableData, Role](mapper=RoleTableMapper())