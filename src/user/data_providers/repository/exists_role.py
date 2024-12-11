from abc import ABC, abstractmethod

class ExistsRole(ABC):
    @abstractmethod
    def exists(self, role: str) -> bool: ...