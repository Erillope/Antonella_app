from src.common import PatternMatcher, StringValue
from src.user.domain.exception import InvalidUserNameException

class UserName:
    __REGREX = "^(?=.{4,16}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def __init__(self, user_name: str) -> None:
        self.__value = StringValue(user_name)
        self.__validate()
    
    def __validate(self) -> None:
        if not self.__MATCHER.match(self.get_value()):
            raise InvalidUserNameException.invalid_name(self.get_value())
    
    def get_value(self) -> str:
        return self.__value.get_value()
    
    def __str__(self) -> str:
        return self.get_value()