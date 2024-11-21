from .user_exception import UserException

class InvalidUserIDException(UserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def invalid_user_id() -> "InvalidUserIDException":
        return InvalidUserIDException("ID Inválido")