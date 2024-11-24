from ....common import RegrexValidator
from ..exception import InvalidPhoneNumberException
from .account import Account

class UserPhoneNumber(Account):
    __REGREX = "^(0)?9\\d{8}$"
    
    def _validate(self, phone_number: str) -> None:
        if not UserPhoneNumber.is_phone_number(phone_number):
            raise InvalidPhoneNumberException.invalid_phone_number(phone_number)
    
    @staticmethod
    def is_phone_number(phone_numer: str) -> bool:
        return RegrexValidator.match(UserPhoneNumber.__REGREX, phone_numer)