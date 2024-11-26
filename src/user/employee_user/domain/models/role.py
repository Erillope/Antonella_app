from src.common import RegrexValidator
from ..exception import InvalidRoleException

class Role:
    __REGREX = "^[a-zA-Z0-9_]{3,20}$"
    
    def __init__(self, role: str) -> None:
        self.__validate_role(role)
        self.__value = role
    
    def __validate_role(self, role: str) -> None:
        if not RegrexValidator.match(self.__REGREX, role):
            raise InvalidRoleException.invalid_role(role)

    def get_value(self) -> str:
        return self.__value
    
    def __str__(self) -> str:
        return str(self.__value)
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Role):
            return self.get_value() == value.get_value()
        return False
    
    def __hash__(self) -> int:
        return hash(self.__value)