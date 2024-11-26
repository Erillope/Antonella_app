from ..dto import SignInDto, EmployeeUserDto
from abc import ABC, abstractmethod

class ISingIn(ABC):
    @abstractmethod
    def sign_in(self, dto: SignInDto) -> EmployeeUserDto: ...