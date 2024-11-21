from .invalid_account_exception import InvalidAccountException

class InvalidUserEmailException(InvalidAccountException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        
    @staticmethod
    def invalid_user_email() -> "InvalidUserEmailException":
        return InvalidUserEmailException("Email Inválido")