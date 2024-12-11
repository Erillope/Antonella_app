from .user_exception import UserException

class InvalidRoleException(UserException):
    @classmethod
    def invalid_role(cls, role: str) -> "InvalidRoleException":
        return cls(f"El rol '{role}' es inválido")