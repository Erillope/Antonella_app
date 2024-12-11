from src.user.domain import Role
from .dto import RoleDto
from datetime import date

class RoleMapper:
    def to_role(self, role: str) -> Role:
        return Role(role, date.today())
    
    def to_dto(self, role: Role) -> RoleDto:
        return RoleDto(role.get_value(), role.get_created_date())