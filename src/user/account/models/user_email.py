from ....common import raises, RegrexValidator
from ..exception import InvalidUserEmailException, InvalidAccountException
from .account import Account
from typing import override

class UserEmail(Account):
    __REGREX = "^[a-zA-Z0-9._%+-]+@gmail\\.com$"
    
    @override
    @raises(InvalidAccountException)
    def _validate(self, email: str) -> None:
        if not UserEmail.is_email(email):
            raise InvalidUserEmailException.invalid_user_email()
    
    @staticmethod
    def is_email(email: str) -> bool:
        return RegrexValidator.match(UserEmail.__REGREX, email)