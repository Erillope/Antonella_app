from src.user.domain import UserAccountFactory, UserAccount, AccountStatus
from .user_account_table_data import UserAccountTableData
from .role_table_mapper import RoleTableMapper
from .role_table_data import RoleTableData
from typing import List

class UserTableMapper:
    def __init__(self) -> None:
        self.__factory = UserAccountFactory()
        self.__role_mapper = RoleTableMapper()
        
    def to_table(self, user: UserAccount) -> UserAccountTableData:
        return UserAccountTableData(
            id = user.get_id(),
            account = user.get_account(),
            name = user.get_name(),
            password = user.get_password(),
            status = user.get_status().name,
            birthdate = user.get_birthdate(),
            created_date = user.get_created_date()
        )
    
    def to_user(self, user_table: UserAccountTableData, roles: List[RoleTableData]) -> UserAccount:
        return self.__factory.load(
            id = str(user_table.id),
            account = user_table.account,
            name = user_table.name,
            password = user_table.password,
            status = AccountStatus(user_table.status),
            birthdate = user_table.birthdate,
            created_date = user_table.created_date,
            roles = [self.__role_mapper.to_role(role) for role in roles]
        )