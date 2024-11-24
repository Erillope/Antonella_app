from ....common import RegrexValidator
from ..exception import InvalidUserPasswordException

class UserPassword:
    __REGREX = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    
    def __init__(self, password: str) -> None:
        self.__validate(password)
        self.__value = password
    
    def __validate(self, password: str) -> None:
        if not RegrexValidator.match(self.__REGREX, password):
            return InvalidUserPasswordException.invalid_password(password)
    
    def get_value(self) -> str:
        return self.__value
    
    def __str__(self) -> str:
        return self.get_value()
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserPassword):
            return self.__value == value.__value
        return False
    
    def __hash__(self) -> int:
        return hash(self.__value)