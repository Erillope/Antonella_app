from .user_exception import UserException
from datetime import date

class InvalidUserBirthdateException(UserException):
    @classmethod
    def invalid_birthdate(cls, birthdate: date) -> "InvalidUserBirthdateException":
        return cls(f"La fecha de nacimiento {birthdate} es inválida")