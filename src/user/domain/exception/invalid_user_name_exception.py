from .user_exception import UserException

class InvalidUserNameException(UserException):
    @classmethod
    def invalid_name(cls, name: str) -> "InvalidUserNameException":
        return cls(f"El nombre de usuario '{name}' es inválido")