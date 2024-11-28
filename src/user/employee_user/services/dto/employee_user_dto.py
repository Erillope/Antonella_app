from src.user.account.services.dto import UserAccountDto
from src.user.account import AccountStatus
from datetime import date
from typing import Set

class EmployeeUserDto(UserAccountDto):
    def __init__(self, id: str, account: str, name: str, roles: Set[str], status: AccountStatus, joined_date: date) -> None:
        super().__init__(id, account, name, status, joined_date)
        self.__roles = roles
    
    def get_roles(self) -> Set[str]:
        return self.__roles
    
    def __str__(self) -> str:
        return f"EmployeeUserDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"roles={self.get_roles()},status={self.get_status()},joined_date={self.get_joined_date()})"