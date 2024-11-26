from .employee_user_auth_exception import EmployeeUserAuthException

class EmployeeIsAlreadyRegisteredException(EmployeeUserAuthException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def is_already_registered(user: str) -> "EmployeeIsAlreadyRegisteredException":
        return EmployeeIsAlreadyRegisteredException(f"El empleado '{user}' ya se encuentra registrado")