from ....common import raises, RegrexValidator
from ..exception import InvalidPhoneNumberException, InvalidAccountException
from .account import Account
from typing import override

class UserPhoneNumber(Account):
    __REGREX = "^(0)?9\\d{8}$"
    
    @override
    @raises(InvalidAccountException)
    def validate(self, phone_number: str) -> None:
        if not UserPhoneNumber.is_phone_number(phone_number):
            raise InvalidPhoneNumberException.invalid_phone_number()
    
    @staticmethod
    def is_phone_number(phone_numer: str) -> bool:
        return RegrexValidator.match(UserPhoneNumber.__REGREX, phone_numer)