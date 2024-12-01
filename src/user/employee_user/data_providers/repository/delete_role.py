from ...domain import Role
from abc import ABC, abstractmethod

class DeleteRole(ABC):
    @abstractmethod
    def delete(self, role: Role) -> Role: ...