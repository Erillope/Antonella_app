from src.common.criteria_filter import OrdenDirection
from .system_exception import SystemException

class InvalidOrderDirectionException(SystemException):
    @classmethod
    def invalid_direction(cls, direction: str) -> "InvalidOrderDirectionException":
        return cls(f"'{direction}'no es una dirección válida. "\
            f"Las direcciones disponibles son {list(OrdenDirection.__members__.keys())}")