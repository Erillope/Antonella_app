from .client_user_repository_exception import ClientUserRepositoryException

class ClientUserNotFoundException(ClientUserRepositoryException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def not_found(client_user: str) -> "ClientUserNotFoundException":
        return ClientUserNotFoundException(f"No se encontró al cliente '{client_user}'")