from rest_framework.request import Request
from src.user.account.services.dto import SignInDto, ChangeDataDto, EnableDto, DisableDto
from src.user.employee_user.services.dto import (RegisterEmployeeDto, GiveRoleDto,
                                                 RemoveRoleDto, AddRoleDto, TakeRoleDto)
from app.user.account.account_request_mapper import AccountRequestMapper
from singleton_decorator import singleton

@singleton
class EmployeeRequestMapper(AccountRequestMapper):    
    def to_register_dto(self, request: Request) -> RegisterEmployeeDto:
        return RegisterEmployeeDto(
            account = request.data.get('account'),
            name = request.data.get('name'),
            roles = request.data.get('roles')
            )
    
    def to_give_role_dto(self, request: Request) -> GiveRoleDto:
        return GiveRoleDto(id = request.data.get('id'), roles = request.data.get('roles'))
    
    def to_take_role_dto(self, request: Request) -> TakeRoleDto:
        return TakeRoleDto(id = request.data.get('id'), roles = request.data.get('roles'))
    
    def to_add_role_dto(self, request: Request) -> AddRoleDto:
        return AddRoleDto(role = request.data.get('role'))
    
    def to_remove_role_dto(self, role: str) -> RemoveRoleDto:
        return RemoveRoleDto(role = role)