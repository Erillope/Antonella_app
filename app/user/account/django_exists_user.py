from src.user.account.data_providers import ExistsUser
from .user_account_table_data import UserAccountTableData
from singleton_decorator import singleton

@singleton
class DjangoExistsUser(ExistsUser):
    def exists_by_account(self, account: str) -> bool:
        return UserAccountTableData.objects.filter(account=account).exists()
    
    def exists_by_id(self, id: str) -> bool:
        return UserAccountTableData.objects.filter(id=id).exists()