from src.user.data_providers import GetRole
from .abstract_get_all_roles import IGetAllRoles
from ..dto import RoleDto
from ..role_mapper import RoleMapper
from typing import List

class GetAllRoles(IGetAllRoles):
    def __init__(self, get_role: GetRole) -> None:
        self.__get_role = get_role
        self.__mapper = RoleMapper()
        
    def get_all(self) -> List[RoleDto]:
        roles = [self.__mapper.to_dto(role) for role in self.__get_role.get_all()]
        return roles