from src.common import PatternMatcher
from src.user.domain.exception import InvalidUserEmailException
from .account import Account

class UserEmail(Account):
    __REGREX = "^[a-zA-Z0-9._%+-]+@gmail\\.com$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def _validate(self) -> None:
        if not UserEmail.is_email(self.get_value()):
            raise InvalidUserEmailException.invalid_user_email(self.get_value())
    
    @classmethod
    def is_email(cls, email: str) -> bool:
        return cls.__MATCHER.match(email)