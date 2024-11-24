from src.user.account import AccountStatus, UserID
from .client_user import ClientUser
from datetime import date

class ClientUserFactory:
    @staticmethod
    def create(id: str, account: str, name: str, password: str,
               birthdate: date, status: AccountStatus, joined_date: date) -> ClientUser:
        return ClientUser(id, account, name, password, birthdate, status, joined_date)
    
    @staticmethod
    def create_default(account: str, name: str, password: str, birthdate: date) -> ClientUser:
        return ClientUser(UserID.generate(), account, name, password, birthdate, AccountStatus.ENABLE,
                          date.today())