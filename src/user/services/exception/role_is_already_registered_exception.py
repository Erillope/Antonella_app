from .user_service_exception import UserServiceException

class RoleIsAlreadyRegisteredException(UserServiceException):
    @classmethod
    def is_already_registered(cls, role: str) -> "RoleIsAlreadyRegisteredException":
        return cls(f"El rol '{role}' ya se encuentra registrado")