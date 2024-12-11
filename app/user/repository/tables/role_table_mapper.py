from src.user.domain import Role
from .role_table_data import RoleTableData

class RoleTableMapper:
    def to_table(self, role: Role) -> RoleTableData:
        return RoleTableData(
            role = role.get_value(),
            created_date = role.get_created_date()
        )
    
    def to_role(self, role_table: RoleTableData) -> Role:
        return Role(
            role = role_table.role,
            created_date = role_table.created_date
        )