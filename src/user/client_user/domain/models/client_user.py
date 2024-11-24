from src.user.account import UserAccount, AccountStatus
from .user_birthdate import UserBirthdate
from datetime import date

class ClientUser(UserAccount):
    def __init__(self, id: str, account: str, name: str, password: str, 
                 birthdate: date, status: AccountStatus, joined_date: date) -> None:
        super().__init__(id, account, name, password, status, joined_date)
        self.__birthdate = UserBirthdate(birthdate)
    
    def get_birthdate(self) -> date:
        return self.__birthdate.get_value()
    
    def __str__(self) -> str:
        return f"ClientUser(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"password={self.get_password()},birthdate={self.get_birthdate()},status={self.get_status()},"\
        f"joined_date={self.get_joined_date()})"