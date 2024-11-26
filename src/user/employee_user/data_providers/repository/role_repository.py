from ...domain import Role
from abc import ABC, abstractmethod
from typing import Set

class RoleRepository(ABC):
    @abstractmethod
    def get_all(self) -> Set[Role]: ...
    
    @abstractmethod
    def save(self, role: Role) -> Role: ...
    
    @abstractmethod
    def remove(self, role: Role) -> Role: ...
    
    @abstractmethod
    def exists(self, role: str) -> bool: ...