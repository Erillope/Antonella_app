from .user_repository_exception import UserRepositoryException

class UserNotFoundException(UserRepositoryException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def not_found(user: str) -> "UserNotFoundException":
        return UserNotFoundException(f"No se encontró al usuario '{user}'")