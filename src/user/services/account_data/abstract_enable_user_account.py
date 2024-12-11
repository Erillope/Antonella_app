from ..dto import EnableDto, UserAccountDto
from abc import ABC, abstractmethod

class IEnableUserAccount(ABC):
    @abstractmethod
    def enable(self, dto: EnableDto) -> UserAccountDto: ...