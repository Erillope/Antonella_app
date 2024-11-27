from .employee_user_service_exception import EmployeeUserServiceException

class EmployeeUserAuthException(EmployeeUserServiceException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)