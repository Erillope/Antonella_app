from ..dto import GiveRoleDto, EmployeeUserDto
from abc import ABC, abstractmethod

class IGiveRole(ABC):
    @abstractmethod
    def give(self, dto: GiveRoleDto) -> EmployeeUserDto: ...