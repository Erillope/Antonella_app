from src.user.account.services.user_account_mapper import UserAccountMapper
from ..domain import EmployeeUser, EmployeeUserFactory, Role
from .dto import RegisterEmployeeDto, EmployeeUserDto, RoleDto
from singleton_decorator import singleton

@singleton
class EmployeeUserMapper(UserAccountMapper):
    def to_user(self, dto: RegisterEmployeeDto) -> EmployeeUser:
        return EmployeeUserFactory.create_default(
            account = dto.get_account(),
            name = dto.get_name()
        )
    
    def to_dto(self, user: EmployeeUser) -> EmployeeUserDto:
        return EmployeeUserDto(
            id = user.get_id(),
            account = user.get_account(),
            name = user.get_name(),
            roles = user.get_roles(),
            status = user.get_status(),
            joined_date = user.get_joined_date()
        )
    
    def to_role_dto(self, role: Role) -> RoleDto:
        return RoleDto(
            role = role.get_value()
        )