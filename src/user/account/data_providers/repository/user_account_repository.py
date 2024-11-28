from ...domain import UserAccount
from abc import ABC, abstractmethod
from typing import List

class UserAccountRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[UserAccount]: ...
    
    @abstractmethod
    def get_by_account(self, account: str) -> UserAccount: ...
    
    @abstractmethod
    def get_by_id(self, id: str) -> UserAccount: ...
    
    @abstractmethod
    def save(self, user: UserAccount) -> UserAccount: ...
    
    @abstractmethod
    def exists_by_account(self, account: str) -> bool: ...
    
    @abstractmethod
    def exists_by_id(self, id: str) -> bool: ...