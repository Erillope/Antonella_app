from src.user.account.services.exception import UserServiceException

class RoleIsAlreadyRegisteredException(UserServiceException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def is_already_registered(role: str) -> "RoleIsAlreadyRegisteredException":
        return RoleIsAlreadyRegisteredException(f"El rol '{role}' ya se encuentra registrado")