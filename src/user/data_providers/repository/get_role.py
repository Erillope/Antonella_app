from ...domain import Role
from abc import ABC, abstractmethod
from typing import List

class GetRole(ABC):
    @abstractmethod
    def get(self, role: str) -> Role: ...
    
    @abstractmethod
    def get_all(self) -> List[Role]: ...