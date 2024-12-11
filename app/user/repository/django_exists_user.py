from src.user import ExistsUser
from .tables import UserAccountTableData

class DjangoExistsUser(ExistsUser):
    def exists_by_account(self, account: str) -> bool:
        return UserAccountTableData.objects.filter(account=account).exists()
    
    def exists_by_id(self, id: str) -> bool:
        return UserAccountTableData.objects.filter(id=id).exists()