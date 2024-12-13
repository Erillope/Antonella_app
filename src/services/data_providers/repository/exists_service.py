from abc import ABC, abstractmethod

class ExistsService(ABC):
    @abstractmethod
    def exists_by_id(self, id: str) -> bool: ...