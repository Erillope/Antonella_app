from .invalid_account_exception import InvalidAccountException

class InvalidUserEmailException(InvalidAccountException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        
    @staticmethod
    def invalid_user_email(email: str) -> "InvalidUserEmailException":
        return InvalidUserEmailException(f"El email '{email}' es inválido")