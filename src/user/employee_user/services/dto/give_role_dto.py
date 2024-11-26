from typing import Set

class GiveRoleDto:
    def __init__(self, id: str, roles: Set[str]) -> None:
        self.__id = id
        self.__roles = roles
    
    def get_id(self) -> str:
        return self.__id
    
    def get_roles(self) -> Set[str]:
        return self.__roles
    
    def __str__(self) -> str:
        return f"GiveRoleDto(id={self.get_id()},roles={self.get_roles()})"