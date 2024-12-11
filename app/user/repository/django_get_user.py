from src.common import OrdenDirection
from app.filter import DjangoFilter
from src.user import GetUser, UserAccount, ExistsUser, UserNotFoundException
from .tables import UserAccountTableData, UserTableMapper, UserRoleTableData
from typing import List

class DjangoGetUser(GetUser):
    def __init__(self, exists_user: ExistsUser) -> None:
        self.__mapper = UserTableMapper()
        self.__exists_user = exists_user
        
    def get_by_account(self, account: str) -> UserAccount:
        if self.__exists_user.exists_by_account(account):
            user_table = UserAccountTableData.objects.get(account=account)
            roles = UserRoleTableData.get_roles_from_user(user_table)
            return self.__mapper.to_user(user_table, roles)
        raise UserNotFoundException.not_found(account)
    
    def get_by_id(self, id: str) -> UserAccount:
        if self.__exists_user.exists_by_id(id):
            user_table = UserAccountTableData.objects.get(id=id)
            roles = UserRoleTableData.get_roles_from_user(user_table)
            return self.__mapper.to_user(user_table, roles)
        raise UserNotFoundException.not_found(id)
    
    def filter(self, expresion: str, limit: int, offset: int,
                 order_by: str, direction: OrdenDirection) -> List[UserAccount]:
        _filter = DjangoUserFilter.construct_filter(UserAccountTableData, expresion,
                                                limit, offset, order_by, direction)
        user_tables = _filter.filter()
        users : List[UserAccount] = []
        for table in user_tables:
            roles = UserRoleTableData.get_roles_from_user(table)
            user = self.__mapper.to_user(table, roles)
            users.append(user)
        return users

class DjangoUserFilter(DjangoFilter):
    fields = ['name', 'status', 'birthdate', 'created_date']