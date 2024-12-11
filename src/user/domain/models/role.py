from src.common import PatternMatcher, StringValue
from ..exception import InvalidRoleException
from datetime import date

class Role:
    __REGREX = "^[a-zA-Z0-9_]{3,20}$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def __init__(self, role: str, created_date: date) -> None:
        self.__value = StringValue(role)
        self.__created_date = created_date
        self.__validate_role()
    
    def __validate_role(self) -> None:
        if not self.__MATCHER.match(self.get_value()):
            raise InvalidRoleException.invalid_role(self.get_value())

    def rename(self, role: str) -> None:
        self.__value = StringValue(role)
        self.__validate_role()
        
    def get_value(self) -> str:
        return self.__value.get_value()
    
    def get_created_date(self) -> date:
        return self.__created_date
    
    def __str__(self) -> str:
        return f"Role(value={self.get_value()},created_date={self.get_created_date()})"
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Role):
            return self.get_value() == value.get_value()
        return False
    
    def __hash__(self) -> int:
        return hash(self.__value)