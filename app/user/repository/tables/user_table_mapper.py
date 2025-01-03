from src.user.domain import UserAccountFactory, UserAccount, AccountStatus
from app.common import TableMapper
from .user_account_table_data import UserAccountTableData

class UserTableMapper(TableMapper[UserAccountTableData, UserAccount]):
    def __init__(self) -> None:
        self.__factory = UserAccountFactory()
        
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
    
    def to_model(self, user_table: UserAccountTableData) -> UserAccount:
        return self.__factory.load(
            id = str(user_table.id),
            account = user_table.account,
            name = user_table.name,
            password = user_table.password,
            status = AccountStatus(user_table.status),
            birthdate = user_table.birthdate,
            created_date = user_table.created_date,
        )