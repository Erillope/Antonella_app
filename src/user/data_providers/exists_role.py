from src.common.repository import ExistsModel
from abc import ABC, abstractmethod

class ExistsRole(ExistsModel, ABC):
    @abstractmethod
    def exists_by_name(self, role: str) -> bool: ...