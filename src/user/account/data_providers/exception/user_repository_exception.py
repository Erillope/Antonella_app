from src.user.account import UserException

class UserRepositoryException(UserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)