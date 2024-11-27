from ..dto import TakeRoleDto, EmployeeUserDto
from abc import ABC, abstractmethod

class ITakeRole(ABC):
    @abstractmethod
    def take(self, dto: TakeRoleDto) -> EmployeeUserDto: ...