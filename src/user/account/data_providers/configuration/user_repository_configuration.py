from ..repository import GetUser, SaveUser, ExistsUser
from abc import ABC, abstractmethod

class UserRepositoryConfiguration(ABC):    
    @abstractmethod
    def construct_get_user(self) -> GetUser: ...
    
    @abstractmethod
    def construct_save_user(self) -> SaveUser: ...
    
    @abstractmethod
    def construct_exists_user(self) -> ExistsUser: ...