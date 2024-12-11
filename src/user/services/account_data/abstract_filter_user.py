from ..dto import FilterUserDto, UserAccountDto
from abc import ABC, abstractmethod
from typing import List

class IFilterUser(ABC):
    @abstractmethod
    def filter(self, dto: FilterUserDto) -> List[UserAccountDto]: ...