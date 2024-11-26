from ..dto import EnableDto, EmployeeUserDto
from abc import ABC, abstractmethod

class IEnableEmployeeUserAccount(ABC):
    @abstractmethod
    def enable(self, dto: EnableDto) -> EmployeeUserDto: ...