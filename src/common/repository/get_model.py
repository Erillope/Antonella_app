from src.common import OrdenDirection
from abc import ABC, abstractmethod
from .typing import Model
from typing import Generic, List, Optional

class GetModel(ABC, Generic[Model]):
    @abstractmethod
    def get_all(self) -> List[Model]: ...
    
    @abstractmethod
    def get_by_id(self, id: str) -> Model: ...
    
    @abstractmethod
    def filter(self, expresion: Optional[str], limit: int, offset: int,
               order_by: str, direction: OrdenDirection) -> List[Model]: ...