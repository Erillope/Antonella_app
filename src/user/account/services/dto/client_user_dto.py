from src.user.account import AccountStatus
from datetime import date

class UserAccountDto:
    def __init__(self, id: str, account: str, name: str, status: AccountStatus, joined_date: date) -> None:
        self.__id = id.strip().lower()
        self.__account = account.strip().lower()
        self.__name = name.strip()
        self.__status = status
        self.__joined_date = joined_date
        
    def get_id(self) -> str:
        return self.__id
    
    def get_account(self) -> str:
        return self.__account
    
    def get_name(self) -> str:
        return self.__name
    
    def get_status(self) -> AccountStatus:
        return self.__status
    
    def get_joined_date(self) -> date:
        return self.__joined_date
    
    def __str__(self) -> str:
        return f"UserAccountDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"status={self.get_status()},joined_date={self.get_joined_date()})"