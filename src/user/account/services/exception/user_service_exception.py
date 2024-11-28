from src.user.account import UserException

class UserServiceException(UserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)