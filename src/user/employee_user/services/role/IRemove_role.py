from ..dto import RemoveRoleDto, RoleDto
from abc import ABC, abstractmethod

class IRemoveRole(ABC):
    @abstractmethod
    def remove(self, dto: RemoveRoleDto) -> RoleDto: ...