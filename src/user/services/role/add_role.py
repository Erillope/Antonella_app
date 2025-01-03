from src.common.repository import SaveModel
from src.user.data_providers import ExistsRole
from src.user.domain import Role
from ..exception import RoleIsAlreadyRegisteredException
from ..mapper import RoleMapper
from ..dto import RoleDto, AddRoleDto
from .abstract_add_role import IAddRole

class AddRole(IAddRole):
    def __init__(self, save_role: SaveModel[Role], exists_role: ExistsRole) -> None:
        self.__save_role = save_role
        self.__exists_role = exists_role
        self.__mapper = RoleMapper()
    
    def add(self, dto: AddRoleDto) -> RoleDto:
        self.__verify_is_already_exists(dto.get_role())
        role = self.__mapper.to_role(dto)
        role = self.__save_role.save(role)
        return self.__mapper.to_dto(role)
        
    def __verify_is_already_exists(self, role: str) -> None:
        if self.__exists_role.exists_by_name(role):
            raise RoleIsAlreadyRegisteredException.is_already_registered(role)