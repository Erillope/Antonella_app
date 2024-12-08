from src.user.client_user.domain import ClientUser, ClientUserFactory
from src.user.account import AccountStatus
from .client_user_table_data import ClientUserTableData
from singleton_decorator import singleton

@singleton
class ClientUserTableMapper:
    def to_table(self, user: ClientUser) -> ClientUserTableData:
        return ClientUserTableData(
            id = user.get_id(),
            account = user.get_account(),
            name = user.get_name(),
            password = user.get_password(),
            birthdate = user.get_birthdate(),
            status = user.get_status().value,
            joined_date = user.get_joined_date()
        )
    
    def to_user(self, user_table: ClientUserTableData) -> ClientUser:
        return ClientUserFactory.create(str(user_table.id), user_table.account, user_table.name,
                                        user_table.password, user_table.birthdate,
                                        AccountStatus(user_table.status), user_table.joined_date)
    