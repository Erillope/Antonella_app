from abc import ABC, abstractmethod
from .typing import Model
from typing import Generic

class DeleteModel(ABC, Generic[Model]):
    @abstractmethod
    def delete(self, id: str) -> Model: ...