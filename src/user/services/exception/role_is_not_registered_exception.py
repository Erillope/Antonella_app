from .user_service_exception import UserServiceException

class RoleIsNotRegisteredException(UserServiceException):
    @classmethod
    def is_not_registered(cls, role: str) -> "RoleIsNotRegisteredException":
        return cls(f"El rol '{role}' no se encuentra registrado")