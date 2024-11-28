from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account: str) -> None:
        account = account.strip().lower()
        self._validate(account)
        self.__value = account
    
    @abstractmethod
    def _validate(self, account: str) -> None: ...
    
    def get_value(self) -> str:
        return self.__value
    
    def __str__(self) -> str:
        return self.get_value()
    
    def __hash__(self) -> int:
        return hash(self.__value)