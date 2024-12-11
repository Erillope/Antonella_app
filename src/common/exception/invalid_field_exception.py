from .system_exception import SystemException
from typing import List

class InvalidFieldException(SystemException):
    @classmethod
    def invalid_field(cls, field: str, fields: List[str]) -> "InvalidFieldException":
        return cls(f"El campo '{field}' es inválido. Los campos válidos son: {fields}")