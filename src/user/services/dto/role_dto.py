from src.common import StringValue
from datetime import date

class RoleDto:
    def __init__(self, role: str, created_date: date) -> None:
        self.__role = StringValue(role)
        self.__created_date = created_date
    
    def get_role(self) -> str:
        return self.__role.get_value()
    
    def get_created_date(self) -> date:
        return self.__created_date
    
    def __str__(self) -> str:
        return f"RoleDto(role={self.get_role()},created_date={self.get_created_date()})"