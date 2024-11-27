from src.user.account import UserAccount
from src.user.account.models.account_status import AccountStatus
from .role import Role
from datetime import date
from typing import Set

class EmployeeUser(UserAccount):
    def __init__(self, id: str, account: str, name: str, password: str, roles: Set[str], status: AccountStatus, joined_date: date) -> None:
        super().__init__(id, account, name, password, status, joined_date)
        self.__roles = set([Role(role) for role in roles])
    
    def get_roles(self) -> Set[str]:
        return set([role.get_value() for role in self.__roles])
    
    def add_role(self, role: str) -> None:
        self.__roles.add(Role(role))
        
    def add_roles(self, roles: Set[str]) -> None:
        for role in roles:
            self.add_role(role)
    
    def remove_role(self, role: str) -> None:
        self.__roles.remove(Role(role))
        
    def remove_roles(self, roles: Set[str]) -> None:
        for role in roles:
            self.remove_role(role)
    
    def have_roles(self) -> bool:
        return len(self.__roles) > 0
    
    def have_role(self, role: str) -> bool:
        return Role(role) in self.__roles
    
    def have_all_roles(self, roles: Set[str]) -> bool:
        for role in roles:
            if not self.have_role(role):
                return False
        return True
    
    def __str__(self) -> str:
        return f"EmployeeUser(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"password={self.get_password()},roles={self.get_roles()},status={self.get_status()},"\
        f"joined_date={self.get_joined_date()})"