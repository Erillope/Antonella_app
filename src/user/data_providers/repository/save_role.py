from src.user.domain import Role
from abc import ABC, abstractmethod

class SaveRole(ABC):
    @abstractmethod
    def save(self, role: Role) -> Role: ...