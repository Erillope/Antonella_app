from src.user.client_user.data_providers import ClientUserRepository, ClientUserNotFoundException
from src.user.client_user.domain import ClientUser
from src.common import override
from .client_user_table_data import ClientUserTableData
from .client_user_table_adapter import ClientUserTableAdapter
from typing import List
from singleton_decorator import singleton

@singleton
class DjangoClientUserRepository(ClientUserRepository):
    @override
    def get_all(self) -> List[ClientUser]:
        user_tables = ClientUserTableData.objects.all()
        users = [ClientUserTableAdapter.to_client_user(user_table) for user_table in user_tables]
        return users
    
    @override
    def get_by_account(self, account: str) -> ClientUser:
        if self.exists_by_account(account):
            user_table = ClientUserTableData.objects.get(account=account)
            user = ClientUserTableAdapter.to_client_user(user_table)
            return user
        else:
            raise ClientUserNotFoundException.not_found(account)
    
    @override
    def get_by_id(self, id: str) -> ClientUser:
        if self.exists_by_id(id):
            user_table = ClientUserTableData.objects.get(id=id)
            user = ClientUserTableAdapter.to_client_user(user_table)
            return user
        else:
            raise ClientUserNotFoundException.not_found(id)
    
    @override
    def save(self, user: ClientUser) -> ClientUser:
        user_table = ClientUserTableAdapter.to_client_user_table(user)
        user_table.save()
        saved_user = ClientUserTableAdapter.to_client_user(user_table)
        return saved_user
    
    @override
    def exists_by_account(self, account: str) -> bool:
        return ClientUserTableData.objects.filter(account=account).exists()
    
    @override
    def exists_by_id(self, id: str) -> bool:
        return ClientUserTableData.objects.filter(id=id).exists()