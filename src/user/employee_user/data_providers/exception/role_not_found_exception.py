from ...domain import EmployeeUserException

class RoleNotFoundException(EmployeeUserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def not_found(role: str) -> "RoleNotFoundException":
        return RoleNotFoundException(f"El rol '{role}' no se encontró")