from .create_view import ViewCreator
from abc import ABC, abstractmethod
from typing import List

class Controller(ABC):
    route_prefix: str = ...
    
    @abstractmethod
    def generate_views(self) -> List[ViewCreator]: ...