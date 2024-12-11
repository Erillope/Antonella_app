from .user_repository_exception import UserRepositoryException

class RoleNotFoundException(UserRepositoryException):
    @classmethod
    def not_found(cls, role: str) -> "RoleNotFoundException":
        return cls(f"No se encontró el rol '{role}'")