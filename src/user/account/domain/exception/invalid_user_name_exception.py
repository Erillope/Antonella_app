from .user_exception import UserException

class InvalidUserNameException(UserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def invalid_name(name: str) -> "InvalidUserNameException":
        return InvalidUserNameException(f"El nombre de usuario '{name}' es inválido")