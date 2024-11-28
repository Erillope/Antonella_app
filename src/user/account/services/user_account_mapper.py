from src.user.account import UserAccount
from .dto import UserAccountDto, SignUpDto
from abc import ABC, abstractmethod

class UserAccountMapper(ABC):
    @abstractmethod
    def to_user(self, dto: SignUpDto) -> UserAccount: ...
    
    @abstractmethod
    def to_dto(self, user: UserAccount) -> UserAccountDto: ...