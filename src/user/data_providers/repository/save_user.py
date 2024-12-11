from ...domain import UserAccount
from abc import ABC, abstractmethod

class SaveUser(ABC):    
    @abstractmethod
    def save(self, user: UserAccount) -> UserAccount: ...