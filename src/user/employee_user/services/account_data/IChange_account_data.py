from ..dto import ChangeDataDto, EmployeeUserDto
from abc import ABC, abstractmethod

class IChangeAccountData(ABC):
    @abstractmethod
    def change_data(self, dto: ChangeDataDto) -> EmployeeUserDto: ...