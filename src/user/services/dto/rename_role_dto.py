from src.common import StringValue

class RenameRoleDto:
    def __init__(self, role: str, new_role: str) -> None:
        self.__role = StringValue(role)
        self.__new_role = StringValue(new_role)
    
    def get_role(self) -> str:
        return self.__role.get_value()
    
    def get_new_role(self) -> str:
        return self.__new_role.get_value()
    
    def __str__(self) -> str:
        return f"RenameRoleDto(role={self.get_role()},new_role={self.get_new_role()})"