from ..exception import InvalidAccountException
from .user_id import UserID
from .user_email import UserEmail
from .account_status import AccountStatus
from .user_name import UserName
from .user_password import UserPassword
from .user_phone_number import UserPhoneNumber
from abc import ABC
from datetime import date

class UserAccount(ABC):
    def __init__(self, id: str, account: str, name: str, password: str, status: AccountStatus, joined_date: date) -> None:
        self.__id = UserID(id)
        self.change_account(account)
        self.change_name(name)
        self.change_password(password)
        self.__status = status
        self.__joined_date = joined_date
    
    def change_account(self, account: str) -> None:
        if account == None or len(account.strip()) == 0: return
        if UserEmail.is_email(account): self.__account = UserEmail(account)
        elif UserPhoneNumber.is_phone_number(account): self.__account = UserPhoneNumber(account)
        else: raise InvalidAccountException.invalid_account(account)
    
    def change_name(self, name: str) -> None:
        if name == None or len(name.strip()) == 0: return
        self.__name = UserName(name)
    
    def change_password(self, password: str) -> None:
        if password == None or len(password.strip()) == 0: return
        self.__password = UserPassword(password)
    
    def enable(self) -> None:
        self.__status = AccountStatus.ENABLE
    
    def disable(self) -> None:
        self.__status = AccountStatus.DISABLE
    
    def is_enable(self) -> bool:
        return self.__status == AccountStatus.ENABLE
    
    def verify_password(self, password: str) -> bool:
        return self.__password == UserPassword(password)

    def get_id(self) -> str:
        return self.__id.get_value()
    
    def get_account(self) -> str:
        return self.__account.get_value()
    
    def get_name(self) -> str:
        return self.__name.get_value()
    
    def get_password(self) -> str:
        return self.__password.get_value()
    
    def get_status(self) -> AccountStatus:
        return self.__status
    
    def get_joined_date(self) -> date:
        return self.__joined_date
    
    def __str__(self) -> str:
        return f"UserAccount(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"password={self.get_password()},status={self.get_status()}),joined_date={self.get_joined_date()}"
    
    def __hash__(self) -> int:
        return hash(self.__id)
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserAccount):
            return self.get_id() == value.get_id()
        return False