from ..data_providers import RoleRepository
from ..domain import Role
from .exception import RoleIsAlreadyRegisteredException, RoleIsNotRegisteredException
from typing import Set

class RoleIsRegistered:
    @staticmethod
    def is_registered(role_repository: RoleRepository, role: str) -> None:
        roles = role_repository.get_all()
        for _role in roles:
            if _role == Role(role):
                 raise RoleIsAlreadyRegisteredException.is_already_registered(role)

    @staticmethod
    def is_not_registered(role_repository: RoleRepository, role: str) -> None:
        roles = role_repository.get_all()
        for _role in roles:
            if _role == Role(role):
                return
        raise RoleIsNotRegisteredException.is_not_registered(role)
    
    @staticmethod
    def verify_is_all_registered(role_repository: RoleRepository, roles: Set[str]) -> None:
        for role in roles:
            RoleIsRegistered.is_not_registered(role_repository, role)