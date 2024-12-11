from ..dto import RemoveRoleDto, UserAccountDto
from abc import ABC, abstractmethod

class IRemoveRole(ABC):
    @abstractmethod
    def remove(self, dto: RemoveRoleDto) -> UserAccountDto: ...