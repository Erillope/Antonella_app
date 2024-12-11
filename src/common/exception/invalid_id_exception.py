from .system_exception import SystemException

class InvalidIdException(SystemException):
    @classmethod
    def invalid_id(cls, id: str) -> "InvalidIdException":
        return cls(f"El id '{id}' es inválido")