from src.common.repository import ExistsModel
from abc import ABC, abstractmethod

class ExistsUser(ExistsModel, ABC):
    @abstractmethod
    def exists_by_account(self, account: str) -> bool: ...