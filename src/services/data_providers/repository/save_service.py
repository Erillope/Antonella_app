from src.services.domain import Service
from abc import ABC, abstractmethod

class SaveService(ABC):
    @abstractmethod
    def save(self, service: Service) -> Service: ...