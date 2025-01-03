from src.common import ID
from src.user.domain import Role
from ..dto import RoleDto, AddRoleDto
from datetime import date

class RoleMapper:
    def to_role(self, dto: AddRoleDto) -> Role:
        return Role(
            id = ID.generate(),
            role = dto.get_role(),
            created_date = date.today()
        )
    
    def to_dto(self, role: Role) -> RoleDto:
        return RoleDto(
            role = role.get_value(),
            created_date = role.get_created_date()
        )