from ...domain import EmployeeUser
from abc import ABC, abstractmethod
from typing import List

class EmployeeUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[EmployeeUser]: ...
    
    @abstractmethod
    def get_by_account(self, account: str) -> EmployeeUser: ...
    
    @abstractmethod
    def get_by_id(self, id: str) -> EmployeeUser: ...
    
    @abstractmethod
    def save(self, employee: EmployeeUser) -> EmployeeUser: ...
    
    @abstractmethod
    def exists_by_account(self, account: str) -> bool: ...
    
    @abstractmethod
    def exists_by_id(self, id: str) -> bool: ...