from src.common import PatternMatcher, StringValue
from src.user.domain.exception import InvalidPhoneNumberException
from .account import Account

class UserPhoneNumber(Account):
    __REGREX = "^(0)?9\\d{8}$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def _validate(self) -> None:
        if not UserPhoneNumber.is_phone_number(self.get_value()):
            raise InvalidPhoneNumberException.invalid_phone_number(self.get_value())
    
    @classmethod
    def is_phone_number(cls, phone_numer: str) -> bool:
        return cls.__MATCHER.match(phone_numer)