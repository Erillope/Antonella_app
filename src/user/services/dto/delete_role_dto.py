from src.common import StringValue

class DeleteRoleDto:
    def __init__(self, role: str) -> None:
        self.__role = StringValue(role)
    
    def get_role(self) -> str:
        return self.__role.get_value()
    
    def __str__(self) -> str:
        return f"DeleteRoleDto(roles={self.get_role()})"