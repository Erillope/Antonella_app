from .user_exception import UserException

class InvalidUserNameException(UserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def invalid_name() -> "InvalidUserNameException":
        return InvalidUserNameException("Nombre de usuario Inválido")