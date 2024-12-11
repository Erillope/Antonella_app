from .user_exception import UserException

class InvalidUserPasswordException(UserException):
    @classmethod
    def invalid_password(cls, password: str) -> "InvalidUserPasswordException":
        return cls(f"La contraseña '{password}' es inválida")