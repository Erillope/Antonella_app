from src.user import GetRole, Role
from app.common.django_repository import DjangoGetModel, ModelNotFoundException
from .tables import RoleTableData, RoleTableMapper

class DjangoGetRole(GetRole, DjangoGetModel[RoleTableData, Role]):
    def __init__(self) -> None:
        super().__init__(RoleTableData, RoleTableMapper())
        
    def get_by_name(self, name: str) -> Role:
        if RoleTableData.objects.filter(role=name).exists():
            role_table = RoleTableData.objects.get(role=name)
            return self._mapper.to_model(role_table)
        raise ModelNotFoundException.not_found(name)