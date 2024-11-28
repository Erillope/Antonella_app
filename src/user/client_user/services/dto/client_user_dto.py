from src.user.account import AccountStatus
from src.user.account.services.dto import UserAccountDto
from datetime import date

class ClientUserDto(UserAccountDto):
    def __init__(self, id: str, account: str, name: str, birthdate: date, 
                 status: AccountStatus, joined_date: date) -> None:
        super().__init__(id, account, name, status, joined_date)
        self.__birthdate = birthdate
    
    def get_birthdate(self) -> date:
        return self.__birthdate
    
    def __str__(self) -> str:
        return f"ClientUserDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"birthdate={self.get_birthdate()},status={self.get_status()},joined_date={self.get_joined_date()})"