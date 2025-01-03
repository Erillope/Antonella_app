from src.common.repository import DeleteModel
from src.user.domain import Role
from abc import ABC, abstractmethod

class DeleteRole(DeleteModel[Role], ABC):
    @abstractmethod
    def delete_by_name(self, role: str) -> Role: ...