from .user_exception import UserException

class InvalidUserPasswordException(UserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def invalid_password() -> "InvalidUserPasswordException":
        return InvalidUserPasswordException("Contraseña Inválida")