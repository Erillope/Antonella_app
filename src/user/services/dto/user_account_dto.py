from src.common import StringValue
from src.user.domain import AccountStatus
from datetime import date
from typing import List

class UserAccountDto:
    def __init__(self, id: str, account: str, name: str, status: AccountStatus,
                 birthdate: date, roles: List[str], created_date: date) -> None:
        self.__id = StringValue(id)
        self.__account = StringValue(account)
        self.__name = StringValue(name, lower=False)
        self.__status = status
        self.__birthdate = birthdate
        self.__roles = roles
        self.__created_date = created_date
        
    def get_id(self) -> str:
        return self.__id.get_value()
    
    def get_account(self) -> str:
        return self.__account.get_value()
    
    def get_name(self) -> str:
        return self.__name.get_value()
    
    def get_status(self) -> AccountStatus:
        return self.__status
    
    def get_birthdate(self) -> date:
        return self.__birthdate
    
    def get_roles(self) -> List[str]:
        return self.__roles
    
    def get_created_date(self) -> date:
        return self.__created_date
    
    def __str__(self) -> str:
        return f"UserAccountDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"status={self.get_status()},birthdate={self.get_birthdate()},roles={self.get_roles()},"\
        f"created_date={self.get_created_date()})"