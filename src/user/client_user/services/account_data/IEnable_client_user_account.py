from ..dto import EnableDto, ClientUserDto
from abc import ABC, abstractmethod

class IEnableClientUserAccount(ABC):
    @abstractmethod
    def enable(self, dto: EnableDto) -> ClientUserDto: ...