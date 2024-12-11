from .user_auth_exception import UserAuthException

class UserIsAlreadyRegisteredException(UserAuthException):
    @classmethod
    def is_already_registered(cls, user: str) -> "UserIsAlreadyRegisteredException":
        return cls(f"El usuario '{user}' ya se encuentra registrado")