from ..dto import SignInDto, ClientUserDto
from abc import ABC, abstractmethod

class ISingIn(ABC):
    @abstractmethod
    def sign_in(self, dto: SignInDto) -> ClientUserDto: ...