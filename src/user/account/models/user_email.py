from ....common import RegrexValidator
from ..exception import InvalidUserEmailException
from .account import Account

class UserEmail(Account):
    __REGREX = "^[a-zA-Z0-9._%+-]+@gmail\\.com$"
    
    def _validate(self, email: str) -> None:
        if not UserEmail.is_email(email):
            raise InvalidUserEmailException.invalid_user_email(email)
    
    @staticmethod
    def is_email(email: str) -> bool:
        return RegrexValidator.match(UserEmail.__REGREX, email)