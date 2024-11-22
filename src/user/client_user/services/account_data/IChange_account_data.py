from ..dto import ChangeDataDto, ClientUserDto
from abc import ABC, abstractmethod

class IChangeAccountData(ABC):
    @abstractmethod
    def changeData(self, dto: ChangeDataDto) -> ClientUserDto: ...