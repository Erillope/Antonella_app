from ..dto import GiveRoleDto, UserAccountDto
from abc import ABC, abstractmethod

class IGiveRole(ABC):
    @abstractmethod
    def give(self, dto: GiveRoleDto) -> UserAccountDto: ...