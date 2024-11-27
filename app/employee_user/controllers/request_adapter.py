from rest_framework.request import Request
from src.user.employee_user.services.dto import (SignInDto, RegisterEmployeeDto, ChangeDataDto, EnableDto,
                                                 DisableDto, GiveRoleDto, RemoveRoleDto, AddRoleDto,
                                                 TakeRoleDto)

class RequestAdapter:
    @staticmethod
    def to_sign_in_dto(request: Request) -> SignInDto:
        return SignInDto(
            account = request.data.get('account'),
            password = request.data.get('password')
            )
    
    @staticmethod
    def to_register_dto(request: Request) -> RegisterEmployeeDto:
        return RegisterEmployeeDto(
            account = request.data.get('account'),
            name = request.data.get('name'),
            roles = request.data.get('roles')
            )
    
    @staticmethod
    def to_change_data_dto(request: Request) -> ChangeDataDto:
        return ChangeDataDto(
            id = request.data.get('id'),
            account = request.data.get('account'),
            name = request.data.get('name'),
            password = request.data.get('password')
        )
    
    @staticmethod
    def to_enable_dto(request: Request) -> EnableDto:
        return EnableDto(id = request.data.get('id'))
    
    @staticmethod
    def to_disable_dto(request: Request) -> DisableDto:
        return DisableDto(id = request.data.get('id'))
    
    @staticmethod
    def to_give_role_dto(request: Request) -> GiveRoleDto:
        return GiveRoleDto(id = request.data.get('id'), roles = request.data.get('roles'))
    
    @staticmethod
    def to_take_role_dto(request: Request) -> TakeRoleDto:
        return TakeRoleDto(id = request.data.get('id'), roles = request.data.get('roles'))
    
    @staticmethod
    def to_add_role_dto(request: Request) -> AddRoleDto:
        return AddRoleDto(role = request.data.get('role'))
    
    @staticmethod
    def to_remove_role_dto(role: str) -> RemoveRoleDto:
        return RemoveRoleDto(role = role)