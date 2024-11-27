from typing import Set

class TakeRoleDto:
    def __init__(self, id: str, roles: Set[str]) -> None:
        self.__id = id.strip()
        self.__roles = roles
    
    def get_id(self) -> str:
        return self.__id
    
    def get_roles(self) -> Set[str]:
        return self.__roles
    
    def __str__(self) -> str:
        return f"TakeRoleDto(id={self.get_id()},roles={self.get_roles()})"