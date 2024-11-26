from ...domain import Role

class RoleDto:
    def __init__(self, role: str) -> None:
        self.__role = role
    
    def get_role(self) -> str:
        return self.__role
    
    @staticmethod
    def generate_dto(role: Role) -> "RoleDto":
        return RoleDto(role.get_value())
    
    def __str__(self) -> str:
        return f"RoleDto(role={self.get_role()})"