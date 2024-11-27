from ...domain import EmployeeUserException

class EmployeeUserRepositoryException(EmployeeUserException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)