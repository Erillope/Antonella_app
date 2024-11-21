from .user_exception import UserException

class InvalidAccountException(UserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        
    @staticmethod
    def invalid_account() -> "InvalidAccountException":
        return InvalidAccountException("Esta cuenta es inválida")