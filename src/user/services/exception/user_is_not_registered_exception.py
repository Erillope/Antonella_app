from .user_auth_exception import UserAuthException

class UserIsNotRegisteredException(UserAuthException):
    @classmethod
    def is_not_registered(cls, user: str) -> "UserIsNotRegisteredException":
        return cls(f"El usuario '{user}' no se encuentra registrado")