from ...domain import UserAccount
from abc import ABC, abstractmethod
from typing import List

class GetUser(ABC):
    @abstractmethod
    def get_all(self) -> List[UserAccount]: ...
    
    @abstractmethod
    def get_by_account(self, account: str) -> UserAccount: ...
    
    @abstractmethod
    def get_by_id(self, id: str) -> UserAccount: ...