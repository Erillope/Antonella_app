from ..repository import ClientUserRepository
from abc import ABC, abstractmethod

class ClientUserRepositoryConfiguration(ABC):    
    @abstractmethod
    def construct_user_repository(self) -> ClientUserRepository: ...