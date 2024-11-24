from .client_user_service_exception import ClientUserServiceException

class ClientUserAuthException(ClientUserServiceException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)