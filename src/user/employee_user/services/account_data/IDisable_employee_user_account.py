from ..dto import DisableDto, EmployeeUserDto
from abc import ABC, abstractmethod

class IDisableEmployeeUserAccount(ABC):
    @abstractmethod
    def disable(self, dto: DisableDto) -> EmployeeUserDto: ...