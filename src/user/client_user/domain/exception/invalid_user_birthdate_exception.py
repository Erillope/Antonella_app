from .client_user_exception import ClientUserException

class InvalidUserBirthdateException(ClientUserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def invalid_birthdate(birthdate: str) -> "InvalidUserBirthdateException":
        return InvalidUserBirthdateException(f"La fecha de nacimiento {birthdate} es inválida")