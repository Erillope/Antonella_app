from .user_auth_exception import UserAuthException

class IncorrectPasswordException(UserAuthException):
    @classmethod
    def incorrect_password(cls, password: str) -> "IncorrectPasswordException":
        return cls(f"La contraseña '{password}' es incorrecta")