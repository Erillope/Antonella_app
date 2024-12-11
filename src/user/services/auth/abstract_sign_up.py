from ..dto import SignUpDto, UserAccountDto
from abc import ABC, abstractmethod

class ISignUp(ABC):
    @abstractmethod
    def sign_up(self, dto: SignUpDto) -> UserAccountDto: ...