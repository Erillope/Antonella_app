from ..dto import DeleteRoleDto, RoleDto
from abc import ABC, abstractmethod

class IDeleteRole(ABC):
    @abstractmethod
    def delete(self, dto: DeleteRoleDto) -> RoleDto: ...