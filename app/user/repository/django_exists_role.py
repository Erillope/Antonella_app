from src.user import ExistsRole
from .tables import RoleTableData

class DjangoExistsRole(ExistsRole):
    def exists(self, role: str) -> bool:
        return RoleTableData.objects.filter(role=role).exists()