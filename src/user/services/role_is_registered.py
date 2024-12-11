from src.user.domain import Role
from src.user.data_providers import ExistsRole, GetRole
from .exception import RoleIsAlreadyRegisteredException, RoleIsNotRegisteredException
from typing import List

class RoleIsRegistered:
    def __init__(self, exists_role: ExistsRole, get_role: GetRole) -> None:
        self.__exists_role = exists_role
        self.__get_role = get_role
    
    def verify_is_already_registered(self, role: str) -> None:
        if self.__exists_role.exists(role):
            raise RoleIsAlreadyRegisteredException.is_already_registered(role)
    
    def is_registered(self, role: str) -> Role:
        if self.__exists_role.exists(role):
            return self.__get_role.get(role)
        raise RoleIsNotRegisteredException.is_not_registered(role)
    
    def verify_is_all_registered(self, roles: List[str]) -> List[Role]:
        return [self.is_registered(role) for role in roles]