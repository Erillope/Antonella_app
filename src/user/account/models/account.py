from ..exception import InvalidAccountException
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account: str) -> None:
        self.__validate(account)
        self.__value = account
    
    @abstractmethod
    def _validate(self, account: str) -> None: ...
    
    def get_value(self) -> str:
        return self.__value
    
    def __str__(self) -> str:
        return self.get_value()
    
    def __hash__(self) -> int:
        return hash(self.__value)