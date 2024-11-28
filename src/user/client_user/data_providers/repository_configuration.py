from src.user.account.data_providers import UserAccountRepository
from abc import ABC, abstractmethod

class ClientUserRepositoryConfiguration(ABC):    
    @abstractmethod
    def construct_user_repository(self) -> UserAccountRepository: ...