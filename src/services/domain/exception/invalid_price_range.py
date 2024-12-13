from .service_exception import ServiceException
from typing import Tuple

class InvalidPriceRangeException(ServiceException):
    @classmethod
    def invalid_price_range(cls, min: int, max: int) -> "InvalidPriceRangeException":
        return cls(f"El rango de precio [{min},{max}] es inválido")