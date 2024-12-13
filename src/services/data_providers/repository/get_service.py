from src.common import OrdenDirection
from src.services.domain import Service
from abc import ABC, abstractmethod
from typing import Optional, List

class GetService(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> Service: ...
    
    @abstractmethod
    def filter(self, expresion: Optional[str], limit: int, offset: int,
               order_by: str, direction: OrdenDirection) -> List[Service]: ...