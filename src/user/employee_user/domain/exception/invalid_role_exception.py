from .employee_user_exception import EmployeeUserException

class InvalidRoleException(EmployeeUserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def invalid_role(role: str) -> "InvalidRoleException":
        return InvalidRoleException(f"El rol '{role}' es inválido")