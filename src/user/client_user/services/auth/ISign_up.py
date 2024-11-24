from ..dto import SignUpDto, ClientUserDto
from abc import ABC, abstractmethod

class ISignUp(ABC):
    @abstractmethod
    def sign_up(self, dto: SignUpDto) -> ClientUserDto: ...