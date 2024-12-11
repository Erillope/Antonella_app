from abc import ABC, abstractmethod

class ExistsUser(ABC):
    @abstractmethod
    def exists_by_account(self, account: str) -> bool: ...
    
    @abstractmethod
    def exists_by_id(self, id: str) -> bool: ...