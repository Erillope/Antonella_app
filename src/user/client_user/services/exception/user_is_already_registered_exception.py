from .client_user_auth_exception import ClientUserAuthException

class UserIsAlreadyRegisteredException(ClientUserAuthException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def is_already_registered(user: str) -> "UserIsAlreadyRegisteredException":
        return UserIsAlreadyRegisteredException(f"El usuario '{user}' ya se encuentra registrado")