from src.common import ID
from ..exception import InvalidAccountException
from .values.user_birthdate import UserBirthdate
from .values.account import Account
from .values.user_email import UserEmail
from .values.account_status import AccountStatus
from .values.user_name import UserName
from .values.user_password import UserPassword
from .values.user_phone_number import UserPhoneNumber
from .role import Role
from abc import ABC
from datetime import date
from typing import List

class UserAccount(ABC):
    def __init__(self, id: str, account: str, name: str, password: str,
                 status: AccountStatus, birthdate: date, created_date: date, roles: List[Role]) -> None:
        self.__account : Account
        self.__id = ID(id)
        self.change_account(account)
        self.change_name(name)
        self.change_password(password)
        self.__status = status
        self.__birthdate = UserBirthdate(birthdate)
        self.__created_date = created_date
        self.__roles = roles
    
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
    
    def is_my_account(self, account: str) -> bool:
        if UserEmail.is_email(account): account = UserEmail(account).get_value()
        elif UserPhoneNumber.is_phone_number(account): account = UserPhoneNumber(account).get_value()
        return account == self.__account.get_value()

    def add_roles(self, roles: List[Role]) -> None:
        for role in roles:
            if role not in self.__roles:
                self.__roles.append(role)
    
    def remove_roles(self, roles: List[Role]) -> None:
        for role in roles:
            if role in self.__roles:
                self.__roles.remove(role)
    
    def have_role(self, role: Role) -> bool:
        return role in self.__roles
    
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
    
    def get_created_date(self) -> date:
        return self.__created_date
    
    def get_birthdate(self) -> date:
        return self.__birthdate.get_value()
    
    def get_roles(self) -> List[Role]:
        return self.__roles
    
    def __str__(self) -> str:
        return f"UserAccount(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"password={self.get_password()},birthdate={self.get_birthdate()},status={self.get_status()},"\
        f"created_date={self.get_created_date()})"