from src.user.account import UserID, UserPassword, AccountStatus
from .employee_user import EmployeeUser
from datetime import date
from typing import Set

class EmployeeUserFactory:
    @staticmethod
    def create(id: str, account: str, name: str, password: str, roles: Set[str], status: AccountStatus, joined_date: date) -> EmployeeUser:
        return EmployeeUser(id, account, name, password, roles, status, joined_date)
    
    @staticmethod
    def create_default(account: str, name: str) -> EmployeeUser:
        return EmployeeUser(UserID.generate(), account, name, UserPassword.generate(), set(),
                            AccountStatus.ENABLE, date.today())