from src.common.repository import GetModel
from src.user.domain import Role
from abc import ABC, abstractmethod

class GetRole(GetModel[Role], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Role: ...