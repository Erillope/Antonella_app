from src.common.repository import GetModel
from src.user.domain import Role
from .abstract_get_all_roles import IGetAllRoles
from ..dto import RoleDto
from ..mapper import RoleMapper
from typing import List

class GetAllRoles(IGetAllRoles):
    def __init__(self, get_role: GetModel[Role]) -> None:
        self.__get_role = get_role
        self.__mapper = RoleMapper()
        
    def get_all(self) -> List[RoleDto]:
        roles = [self.__mapper.to_dto(role) for role in self.__get_role.get_all()]
        return roles