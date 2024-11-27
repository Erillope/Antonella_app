from ...domain import EmployeeUserException

class EmployeeUserNotFoundException(EmployeeUserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    
    @staticmethod
    def not_found(user_account: str) -> "EmployeeUserNotFoundException":
        return EmployeeUserNotFoundException(f"No se encontró al empleado '{user_account}'")