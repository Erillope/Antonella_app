from ....common import raises, RegrexValidator
from ..exception import InvalidUserNameException

class UserName():
    __REGREX = "^(?=.{4,16}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$"
    
    @raises(InvalidUserNameException)
    def __init__(self, user_name: str) -> None:
        self.__validate(user_name)
        self.__value = user_name
    
    @raises(InvalidUserNameException)
    def __validate(self, user_name: str) -> None:
        if not RegrexValidator.match(self.__REGREX, user_name):
            raise InvalidUserNameException.invalid_name()
    
    def get_value(self) -> str:
        return self.__value
    
    def __str__(self) -> str:
        return self.get_value()
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, UserName):
            return self.value == value.value
        return False
    
    def __hash__(self) -> int:
        return hash(self.value)