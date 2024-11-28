from ..dto import ChangeDataDto, UserAccountDto
from abc import ABC, abstractmethod

class IChangeAccountData(ABC):
    @abstractmethod
    def change_data(self, dto: ChangeDataDto) -> UserAccountDto: ...