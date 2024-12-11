from src.common import OrdenDirection
from src.user.domain import UserAccount
from abc import ABC, abstractmethod
from typing import List, Optional

class GetUser(ABC):
    @abstractmethod
    def filter(self, expresion: Optional[str], limit: int, offset: int,
               order_by: str, direction: OrdenDirection) -> List[UserAccount]: ...
    
    @abstractmethod
    def get_by_account(self, account: str) -> UserAccount: ...
    
    @abstractmethod
    def get_by_id(self, id: str) -> UserAccount: ...