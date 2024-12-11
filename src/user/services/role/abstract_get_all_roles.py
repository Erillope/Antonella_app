from ..dto import RoleDto
from abc import ABC, abstractmethod
from typing import List

class IGetAllRoles(ABC):
    @abstractmethod
    def get_all(self) -> List[RoleDto]: ...