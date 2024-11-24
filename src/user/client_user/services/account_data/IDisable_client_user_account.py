from ..dto import DisableDto, ClientUserDto
from abc import ABC, abstractmethod

class IDisableClientUserAccount(ABC):
    @abstractmethod
    def disable(self, dto: DisableDto) -> ClientUserDto: ...