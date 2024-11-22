from src.user.account import UserAccount, AccountState
from .user_birthdate import UserBirthdate
from datetime import date

class ClientUser(UserAccount):
    def __init__(self, id: str, account: str, name: str, password: str, 
                 birthdate: date, state: AccountState) -> None:
        super().__init__(id, account, name, password, state)
        self.__birthdate = UserBirthdate(birthdate)
    
    def get_birthdate(self) -> date:
        return self.__birthdate.get_value()
    
    def __str__(self) -> str:
        return f"ClientUser(id={self.get_id()},account={self.get_account()},name={self.get_name()},
    password={self.get_password()},birthdate={self.get_birthdate()},state={self.get_state()})"