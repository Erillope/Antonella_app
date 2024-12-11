from .user_repository_exception import UserRepositoryException

class UserNotFoundException(UserRepositoryException):
    @classmethod
    def not_found(cls, user: str) -> "UserNotFoundException":
        return cls(f"No se encontró al usuario '{user}'")