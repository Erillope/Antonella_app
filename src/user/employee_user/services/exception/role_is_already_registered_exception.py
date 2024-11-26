from .employee_user_auth_exception import EmployeeUserAuthException

class RoleIsAlreadyRegisteredException(EmployeeUserAuthException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def is_already_registered(role: str) -> "RoleIsAlreadyRegisteredException":
        return RoleIsAlreadyRegisteredException(f"El rol '{role}' ya se encuentra registrado")