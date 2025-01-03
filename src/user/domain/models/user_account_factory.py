from .user_account import UserAccount
from .user_account_builder import UserAccountBuilder
from .role import Role
from .values import AccountStatus
from typing import List, Optional
from datetime import date

class UserAccountFactory:
    def create(self, account: str, name: str, password: str, birthdate: date) -> UserAccount:
        return UserAccountBuilder(
            account = account,
            name = name,
            birthdate = birthdate,
            password = password
        ).build()
    
    def load(self, id: str, account: str, name: str, password: str,
                 status: AccountStatus, birthdate: date, created_date: date) -> UserAccount:
        return UserAccountBuilder(
            account = account,
            name = name,
            birthdate = birthdate,
            password = password
        ).id(id).status(status).created_date(created_date).build()