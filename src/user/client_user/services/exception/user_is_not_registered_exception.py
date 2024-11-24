from .client_user_auth_exception import ClientUserAuthException

class UserIsNotRegisteredException(ClientUserAuthException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        
    @staticmethod
    def is_not_registered(user: str) -> "UserIsNotRegisteredException":
        return UserIsNotRegisteredException(f"El usuario '{user}' no se encuentra registrado")