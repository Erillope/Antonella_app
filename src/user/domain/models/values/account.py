from src.common import StringValue
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account: str) -> None:
        self.__value = StringValue(account)
        self._validate()
    
    @abstractmethod
    def _validate(self) -> None: ...
    
    def get_value(self) -> str:
        return self.__value.get_value()
    
    def __str__(self) -> str:
        return self.get_value()