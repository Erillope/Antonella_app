from src.common import StringValue
from typing import Optional, List
from datetime import date

class SignUpDto:
    def __init__(self, account: str, name: str, password: str, birthdate: date,
                 roles: Optional[List[str]]) -> None:
        self.__account = StringValue(account)
        self.__name = StringValue(name, lower=False)
        self.__password = password
        self.__birthdate = birthdate
        self.__roles = roles
    
    def get_account(self) -> str:
        return self.__account.get_value()
    
    def get_name(self) -> str:
        return self.__name.get_value()
    
    def get_password(self) -> str:
        return self.__password
    
    def get_birthdate(self) -> date:
        return self.__birthdate
    
    def get_roles(self) -> Optional[List[str]]:
        return self.__roles
    
    def __str__(self) -> str:
        return f"SignUpDto(account={self.get_account()},name={self.get_name()},password={self.get_password()}"\
            f",birthdate={self.get_birthdate()},roles={self.get_roles()})"