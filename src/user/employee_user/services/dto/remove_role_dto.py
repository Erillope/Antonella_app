class RemoveRoleDto:
    def __init__(self, role: str) -> None:
        self.__role = role.strip()
    
    def get_role(self) -> str:
        return self.__role
    
    def __str__(self) -> str:
        return f"RemoveRoleDto(roles={self.get_role()})"