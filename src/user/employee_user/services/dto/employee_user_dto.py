from src.user.account import AccountStatus
from ...domain import EmployeeUser
from datetime import date
from typing import Set

class EmployeeUserDto:
    def __init__(self, id: str, account: str, name: str, roles: Set[str], status: AccountStatus, joined_date: date) -> None:
        self.__id = id
        self.__account = account
        self.__name = name
        self.__roles = roles
        self.__status = status
        self.__joined_date = joined_date
    
    @staticmethod
    def generate_dto(employee: EmployeeUser) -> "EmployeeUserDto":
        return EmployeeUserDto(employee.get_id(), employee.get_account(), employee.get_name(),
                             employee.get_roles(), employee.get_status(), employee.get_joined_date())
        
    def get_id(self) -> str:
        return self.__id
    
    def get_account(self) -> str:
        return self.__account
    
    def get_name(self) -> str:
        return self.__name
    
    def get_roles(self) -> Set[str]:
        return self.__roles
    
    def get_status(self) -> AccountStatus:
        return self.__status
    
    def get_joined_date(self) -> date:
        return self.__joined_date
    
    def __str__(self) -> str:
        return f"EmployeeUserDto(id={self.get_id()},account={self.get_account()},name={self.get_name()},"\
    f"roles={self.get_roles()},status={self.get_status()},joined_date={self.get_joined_date()})"