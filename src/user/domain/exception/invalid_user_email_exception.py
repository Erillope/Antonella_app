from .invalid_account_exception import InvalidAccountException

class InvalidUserEmailException(InvalidAccountException):
    @classmethod
    def invalid_user_email(cls, email: str) -> "InvalidUserEmailException":
        return cls(f"El email '{email}' es inválido")