from .system_exception import SystemException
from typing import List

class MissingOperationException(SystemException):
    @classmethod
    def missing_operation(cls, operations: List[str]) -> "MissingOperationException":
        return cls(f"'Falta la operación. Las operaciones disponibles son {operations}")