from .client_user_auth_exception import ClientUserAuthException

class IncorrectPasswordException(ClientUserAuthException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def incorrect_password(password: str) -> "IncorrectPasswordException":
        return IncorrectPasswordException(f"La contraseña '{password}' es incorrecta")