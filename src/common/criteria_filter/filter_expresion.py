from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Model = TypeVar("Model")

class FilterExpresion(ABC, Generic[Model]):
    @abstractmethod
    def and_(self, binary_expresion: str) -> None: ...
    
    @abstractmethod
    def or_(self, binary_expresion: str) -> None: ...
    
    @abstractmethod
    def filter(self) -> Model: ...