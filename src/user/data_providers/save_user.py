from src.common.repository import SaveModel
from src.user.domain import UserAccount, Role
from abc import ABC, abstractmethod
from typing import List

class SaveUser(SaveModel[UserAccount], ABC):
    @abstractmethod
    def give_roles(self, id: str, roles: List[Role]) -> UserAccount: ...
    
    @abstractmethod
    def remove_roles(self, id: str, roles: List[Role]) -> UserAccount: ...