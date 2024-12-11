from src.common import PatternMatcher
from src.user.domain.exception import InvalidUserPasswordException

class UserPassword:
    __REGREX = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def __init__(self, password: str) -> None:
        self.__value = password
        self.__validate()
    
    def __validate(self) -> None:
        if not self.__MATCHER.match(self.get_value()):
            raise InvalidUserPasswordException.invalid_password(self.get_value())
    
    def get_value(self) -> str:
        return self.__value
    
    @staticmethod
    def generate() -> str:
        return "Password_123"
    
    def __str__(self) -> str:
        return self.get_value()
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserPassword):
            return self.get_value() == value.get_value()
        return False