from ..dto import SignInDto, UserAccountDto
from abc import ABC, abstractmethod

class ISignIn(ABC):
    @abstractmethod
    def sign_in(self, dto: SignInDto) -> UserAccountDto: ...