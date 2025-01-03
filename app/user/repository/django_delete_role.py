from src.user import DeleteRole, Role
from app.common.django_repository import DjangoDeleteModel
from .tables import RoleTableData, RoleTableMapper

class DjangoDeleteRole(DeleteRole, DjangoDeleteModel[RoleTableData, Role]):
    def __init__(self) -> None:
        super().__init__(RoleTableData, RoleTableMapper())
        
    def delete_by_name(self, role: str) -> Role:
        role_table = self._table.objects.get(role=role)
        role_model = self._mapper.to_model(role_table)
        role_table.delete()
        return role_model