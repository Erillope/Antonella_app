from ..dto import RegisterEmployeeDto, EmployeeUserDto
from abc import ABC, abstractmethod

class IRegisterEmployee(ABC):
    @abstractmethod
    def register_employee(self, dto: RegisterEmployeeDto) -> EmployeeUserDto: ...