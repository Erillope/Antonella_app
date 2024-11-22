from src.user.account import AccountState, UserID
from .client_user import ClientUser
from datetime import date

class ClientUserFactory:
    @staticmethod
    def create(id: str, account: str, name: str, password: str,
               birthdate: date, state: AccountState) -> ClientUser:
        return ClientUser(id, account, name, password, date, state)
    
    @staticmethod
    def create_default(account: str, name: str, password: str, birthdate: date) -> ClientUser:
        return ClientUser(UserID.generate(), account, name, password, birthdate, AccountState.ENABLE)