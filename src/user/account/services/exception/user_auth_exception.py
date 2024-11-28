from .user_service_exception import UserServiceException

class UserAuthException(UserServiceException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)