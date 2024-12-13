from src.common import AmountValue
from src.services.domain.exception import InvalidPriceRangeException

class PriceRange:
    def __init__(self, min: int, max: int) -> None:
        self.__min = AmountValue(min)
        self.__max = AmountValue(max)
        self.__validate()
    
    def __validate(self) -> None:
        if self.get_min() > self.get_max():
            raise InvalidPriceRangeException.invalid_price_range(self.get_min(), self.get_max())
    
    def get_min(self) -> int:
        return int(self.__min.get_value())
    
    def get_max(self) -> int:
        return int(self.__max.get_value())