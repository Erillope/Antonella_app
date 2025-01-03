from src.common.repository import GetModel
from src.user.domain import UserAccount, Role
from typing import List
from abc import ABC, abstractmethod

class GetUser(GetModel[UserAccount], ABC):
    @abstractmethod
    def get_by_account(self, account: str) -> UserAccount: ...
    
    @abstractmethod
    def get_roles(self, id: str) -> List[Role]: ...