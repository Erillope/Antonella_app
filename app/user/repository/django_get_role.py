from src.user import GetRole, Role, ExistsRole, RoleNotFoundException
from .tables import RoleTableData, RoleTableMapper
from typing import List

class DjangoGetRole(GetRole):
    def __init__(self, exists_role: ExistsRole) -> None:
        self.__mapper = RoleTableMapper()
        self.__exists_role = exists_role
    
    def get(self, role: str) -> Role:
        if self.__exists_role.exists(role):
            role_table =  RoleTableData.objects.get(role=role)
            return self.__mapper.to_role(role_table)
        raise RoleNotFoundException.not_found(role)
    
    def get_all(self) -> List[Role]:
        role_tables = RoleTableData.objects.all()
        roles = [self.__mapper.to_role(role) for role in role_tables]
        return roles