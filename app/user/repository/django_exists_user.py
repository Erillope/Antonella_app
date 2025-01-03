from src.user import ExistsUser
from app.common.django_repository import DjangoExistsModel
from .tables import UserAccountTableData

class DjangoExistsUser(ExistsUser, DjangoExistsModel[UserAccountTableData]):
    def __init__(self) -> None:
        super().__init__(table=UserAccountTableData)
        
    def exists_by_account(self, account: str) -> bool:
        return self._table.objects.filter(account=account).exists()