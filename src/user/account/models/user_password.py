from ....common import raises, RegrexValidator
from ..exception import InvalidUserPasswordException

class UserPassword:
    __REGREX = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    
    @raises(InvalidUserPasswordException)
    def __init__(self, password: str) -> None:
        self.__validate(password)
        self.__value = password
    
    @raises(InvalidUserPasswordException)
    def __validate(self, password: str) -> None:
        if not RegrexValidator.match(self.__REGREX, password):
            return InvalidUserPasswordException.invalid_password()
    
    def get_value(self) -> str:
        return self.__value
    
    def __str__(self) -> str:
        return self.get_value()
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserPassword):
            return self.value == value
        return False
    
    def __hash__(self) -> int:
        return hash(self.value)