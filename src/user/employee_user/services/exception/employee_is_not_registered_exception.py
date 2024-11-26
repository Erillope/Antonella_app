from .employee_user_auth_exception import EmployeeUserAuthException

class EmployeeIsNotRegisteredException(EmployeeUserAuthException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def is_not_registered(user: str) -> "EmployeeIsNotRegisteredException":
        return EmployeeIsNotRegisteredException(f"El empleado '{user}' no se encuentra registrado")