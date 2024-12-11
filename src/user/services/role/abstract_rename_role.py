from ..dto import RenameRoleDto, RoleDto
from abc import ABC, abstractmethod

class IRenameRole(ABC):
    @abstractmethod
    def rename(self, dto: RenameRoleDto) -> RoleDto: ...