from src.common import StringValue
from typing import Optional

class ChangeDataDto:
    def __init__(self, id: str, account: Optional[str], name: Optional[str], password: Optional[str]) -> None:
        self.__id = StringValue(id)
        self.__account : Optional[str] = None
        self.__name : Optional[str] = None
        if account is not None:
            self.__account = StringValue(account).get_value()
        if name is not None:
            self.__name = StringValue(name, lower=False).get_value()
        self.__password = password
    
    def get_id(self) -> str:
        return self.__id.get_value()
    
    def get_account(self) -> Optional[str]:
        return self.__account
    
    def get_name(self) -> Optional[str]:
        return self.__name
    
    def get_password(self) -> Optional[str]:
        return self.__password
    
    def __str__(self) -> str:
        return f"ChangeDataDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"password={self.get_password()})"