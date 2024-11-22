from src.user.client_user.domain import ClientUserException

class ClientUserRepositoryException(ClientUserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)