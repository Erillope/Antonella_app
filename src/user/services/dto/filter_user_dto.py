from src.common import StringValue, OrdenDirection, AmountValue
from typing import Optional

class FilterUserDto:
    def __init__(self, expresion: Optional[str], order_by: str, offset: int,
                 limit: int, direction: OrdenDirection) -> None:
        self.__expresion : Optional[str] = None
        if expresion is not None:
            self.__expresion = StringValue(expresion).get_value()
        self.__order_by = StringValue(order_by)
        self.__offset = AmountValue(offset)
        self.__limit = AmountValue(limit)
        self.__direction = direction
    
    def get_expresion(self) -> Optional[str]:
        return self.__expresion
    
    def get_order_by(self) -> str:
        return self.__order_by.get_value()
    
    def get_offset(self) -> int:
        return int(self.__offset.get_value())
    
    def get_limit(self) -> int:
        return int(self.__limit.get_value())
    
    def get_direction(self) -> OrdenDirection:
        return self.__direction
    
    def __str__(self) -> str:
        return f"FilterUserDto(expresion={self.get_expresion()},order_by={self.get_order_by()},"\
            f"offset={self.get_offset()},limit={self.get_limit()},direction={self.get_direction})"