from src.user import SaveRole, Role
from .tables import RoleTableMapper

class DjangoSaveRole(SaveRole):
    def __init__(self) -> None:
        self.__mapper = RoleTableMapper()
    
    def save(self, role: Role) -> Role:
        role_table = self.__mapper.to_table(role)
        role_table.save()
        role = self.__mapper.to_role(role_table)
        return role