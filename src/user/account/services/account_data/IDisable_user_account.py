from ..dto import DisableDto, UserAccountDto
from abc import ABC, abstractmethod

class IDisableUserAccount(ABC):
    @abstractmethod
    def disable(self, dto: DisableDto) -> UserAccountDto: ...