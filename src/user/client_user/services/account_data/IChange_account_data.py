from ..dto import ChangeDataDto, ClientUserDto
from abc import ABC, abstractmethod

class IChangeAccountData(ABC):
    @abstractmethod
    def change_data(self, dto: ChangeDataDto) -> ClientUserDto: ...