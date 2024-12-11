from src.common import StringValue
from typing import List

class GiveRoleDto:
    def __init__(self, id: str, roles: List[str]) -> None:
        self.__id = StringValue(id)
        self.__roles = roles
    
    def get_id(self) -> str:
        return self.__id.get_value()
    
    def get_roles(self) -> List[str]:
        return self.__roles
    
    def __str__(self) -> str:
        return f"GiveRoleDto(id={self.get_id()},roles={self.get_roles()})"