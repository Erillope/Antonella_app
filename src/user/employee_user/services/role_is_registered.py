from ..data_providers import GetRole
from ..domain import Role
from .exception import RoleIsAlreadyRegisteredException, RoleIsNotRegisteredException
from typing import Set

class RoleIsRegistered:
    def __init__(self, get_role: GetRole) -> None:
        self.__get_role = get_role
        
    def is_registered(self, role: str) -> None:
        roles = self.__get_role.get_all()
        for _role in roles:
            if _role == Role(role):
                 raise RoleIsAlreadyRegisteredException.is_already_registered(role)

    def is_not_registered(self, role: str) -> None:
        roles = self.__get_role.get_all()
        for _role in roles:
            if _role == Role(role):
                return
        raise RoleIsNotRegisteredException.is_not_registered(role)
    
    def verify_is_all_registered(self, roles: Set[str]) -> None:
        for role in roles:
            self.is_not_registered(role)