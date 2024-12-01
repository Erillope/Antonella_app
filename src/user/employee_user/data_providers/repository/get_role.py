from ...domain import Role
from abc import ABC, abstractmethod
from typing import Set

class GetRole(ABC):
    @abstractmethod
    def get_all(self) -> Set[Role]: ...