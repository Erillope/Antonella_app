from .employee_user_auth_exception import EmployeeUserAuthException

class RoleIsNotRegisteredException(EmployeeUserAuthException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def is_not_registered(role: str) -> "RoleIsNotRegisteredException":
        return RoleIsNotRegisteredException(f"El rol '{role}' no se encuentra registrado")