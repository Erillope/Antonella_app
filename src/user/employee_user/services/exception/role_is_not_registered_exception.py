from src.user.account.services.exception import UserServiceException

class RoleIsNotRegisteredException(UserServiceException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def is_not_registered(role: str) -> "RoleIsNotRegisteredException":
        return RoleIsNotRegisteredException(f"El rol '{role}' no se encuentra registrado")