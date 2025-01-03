from src.user import ExistsRole
from app.common.django_repository import DjangoExistsModel
from .tables import RoleTableData

class DjangoExistsRole(ExistsRole, DjangoExistsModel[RoleTableData]):
    def __init__(self) -> None:
        super().__init__(table=RoleTableData)
        
    def exists_by_name(self, role: str) -> bool:
        return self._table.objects.filter(role=role).exists()