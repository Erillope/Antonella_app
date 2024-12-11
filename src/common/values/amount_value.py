from src.common.exception import InvalidAmountException
from decimal import Decimal

class AmountValue:
    def __init__(self, amount: float | Decimal | str):
        self.__amount = Decimal(amount)
        self.__validate()
    
    def __validate(self) -> None:
        if self.__amount < 0:
            raise InvalidAmountException.invalid_amount(self.__amount)
    
    def get_value(self) -> Decimal:
        return self.__amount