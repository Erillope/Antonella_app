from src.services.domain import Service
from abc import ABC, abstractmethod

class DeleteService(ABC):
    @abstractmethod
    def delete(self, id: Service) -> Service: ...