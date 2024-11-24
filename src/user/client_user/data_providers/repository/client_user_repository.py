from ...domain import ClientUser
from abc import ABC, abstractmethod
from typing import List

class ClientUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ClientUser]: ...
    
    @abstractmethod
    def get_by_account(self, account: str) -> ClientUser: ...
    
    @abstractmethod
    def get_by_id(self, id: str) -> ClientUser: ...
    
    @abstractmethod
    def save(self, user: ClientUser) -> ClientUser: ...
    
    @abstractmethod
    def exists_by_account(self, account: str) -> bool: ...
    
    @abstractmethod
    def exists_by_id(self, id: str) -> bool: ...