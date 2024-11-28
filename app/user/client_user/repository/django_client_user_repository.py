from src.user.account.data_providers import UserNotFoundException, UserAccountRepository
from src.user.client_user.domain import ClientUser
from .client_user_table_data import ClientUserTableData
from .client_user_table_mapper import ClientUserTableMapper
from typing import List
from singleton_decorator import singleton

@singleton
class DjangoClientUserRepository(UserAccountRepository):
    def __init__(self) -> None:
        super().__init__()
        self.__mapper = ClientUserTableMapper()
        
    def get_all(self) -> List[ClientUser]:
        user_tables = ClientUserTableData.objects.all()
        users = [self.__mapper.to_user(user_table) for user_table in user_tables]
        return users
    
    def get_by_account(self, account: str) -> ClientUser:
        if self.exists_by_account(account):
            user_table = ClientUserTableData.objects.get(account=account)
            user = self.__mapper.to_user(user_table)
            return user
        else:
            raise UserNotFoundException.not_found(account)
    
    def get_by_id(self, id: str) -> ClientUser:
        if self.exists_by_id(id):
            user_table = ClientUserTableData.objects.get(id=id)
            user = self.__mapper.to_user(user_table)
            return user
        else:
            raise UserNotFoundException.not_found(id)
    
    def save(self, user: ClientUser) -> ClientUser:
        user_table = self.__mapper.to_table(user)
        user_table.save()
        saved_user = self.__mapper.to_user(user_table)
        return saved_user
    
    def exists_by_account(self, account: str) -> bool:
        return ClientUserTableData.objects.filter(account=account).exists()
    
    def exists_by_id(self, id: str) -> bool:
        return ClientUserTableData.objects.filter(id=id).exists()