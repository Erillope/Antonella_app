from abc import ABC, abstractmethod
from .typing import Model
from typing import Generic

class SaveModel(ABC, Generic[Model]):
    @abstractmethod
    def save(self, model: Model) -> Model: ...