from src.common import ID
from .user_account import UserAccount
from .values import AccountStatus, UserPassword
from .role import Role
from datetime import date
from typing import List

class UserAccountBuilder:
    def __init__(self, account: str, name: str, birthdate: date, password: str) -> None:
        self.__id = ID.generate()
        self.__status = AccountStatus.ENABLE
        self.__created_date = date.today()
        self.__roles : List[Role] = []
        self.__password = password
        self.__account = account
        self.__name = name
        self.__birthdate = birthdate
    
    def id(self, id: str) -> "UserAccountBuilder":
        self.__id = id
        return self
    
    def status(self, status: AccountStatus) -> "UserAccountBuilder":
        self.__status = status
        return self
    
    def created_date(self, created_date: date) -> "UserAccountBuilder":
        self.__created_date = created_date
        return self
    
    def roles(self, roles: List[Role]) -> "UserAccountBuilder":
        self.__roles = roles
        return self
    
    def build(self) -> UserAccount:
        return UserAccount(
            id = self.__id,
            account = self.__account,
            name = self.__name,
            password = self.__password,
            status = self.__status,
            birthdate = self.__birthdate,
            created_date = self.__created_date,
            roles = self.__roles
        )