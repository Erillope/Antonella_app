from abc import ABC, abstractmethod

class ExistsModel(ABC):
    @abstractmethod
    def exists(self, id: str) -> bool: ...