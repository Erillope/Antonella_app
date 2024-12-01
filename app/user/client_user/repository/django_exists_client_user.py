from src.user.account.data_providers import ExistsUser
from .client_user_table_data import ClientUserTableData
from singleton_decorator import singleton

@singleton
class DjangoExistsClientUser(ExistsUser):
    def exists_by_account(self, account: str) -> bool:
        return ClientUserTableData.objects.filter(account=account).exists()
    
    def exists_by_id(self, id: str) -> bool:
        return ClientUserTableData.objects.filter(id=id).exists()