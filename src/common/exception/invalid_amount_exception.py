from .system_exception import SystemException
from decimal import Decimal

class InvalidAmountException(SystemException):
    @classmethod
    def invalid_amount(cls, amount: Decimal) -> "InvalidAmountException":
        return cls(f"La cantidad '{amount}' es inválida")