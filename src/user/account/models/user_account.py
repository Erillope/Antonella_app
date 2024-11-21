from ....common import raises
from ..exception import *
from .user_id import UserID
from .user_email import UserEmail
from .account_state import AccountState
from .user_name import UserName
from .user_password import UserPassword
from .user_phone_number import UserPhoneNumber
from abc import ABC

class UserAccount(ABC):
    @raises(UserException)
    def __init__(self, id: str, account: str, name: str, password: str, state: AccountState) -> None:
        self.__id = UserID(id)
        self.change_account(account)
        self.change_name(name)
        self.change_password(password)
        self.__state = state
    
    @raises(InvalidAccountException)
    def change_account(self, account: str) -> None:
        if account == None: return
        if UserEmail.is_email(account): self.__account = UserEmail(account)
        elif UserPhoneNumber.is_phone_number(account): self.__account = UserPhoneNumber(account)
        else: raise InvalidAccountException.invalid_account()
    
    @raises(InvalidUserNameException)
    def change_name(self, name: str) -> None:
        if name == None: raise InvalidUserNameException.invalid_name()
        self.__name = UserName(name)
    
    @raises(InvalidUserPasswordException)
    def change_password(self, password: str) -> None:
        if password == None: raise InvalidUserPasswordException.invalid_password()
        self.__password = UserPassword(password)
    
    def enable(self) -> None:
        self.__state = AccountState.ENABLE
    
    def disable(self) -> None:
        self.__state = AccountState.DISABLE
    
    def is_enable(self) -> bool:
        return self.__state == AccountState.ENABLE

    def get_id(self) -> str:
        return self.__id.get_value()
    
    def get_account(self) -> str:
        return self.__account.get_value()
    
    def get_name(self) -> str:
        return self.__name.get_value()
    
    def get_password(self) -> str:
        return self.__password.get_value()
    
    def get_state(self) -> AccountState:
        return self.__state
    
    def __str__(self) -> str:
        return f"UserAccount(id={self.get_id()},account={self.get_account()},name={self.get_name()},
    password={self.get_password()},state={self.get_state()})"
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserAccount):
            return self.get_id() == value.get_id()
        return False