from src.user import DeleteRole, Role
from .tables import RoleTableMapper

class DjangoDeleteRole(DeleteRole):
    def __init__(self) -> None:
        self.__mapper = RoleTableMapper()
    
    def delete(self, role: Role) -> Role:
        role_table = self.__mapper.to_table(role)
        role = self.__mapper.to_role(role_table)
        role_table.delete()
        return role