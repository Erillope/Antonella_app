from ..dto import AddRoleDto, RoleDto
from abc import ABC, abstractmethod

class IAddRole(ABC):
    @abstractmethod
    def add(self, dto: AddRoleDto) -> RoleDto: ...