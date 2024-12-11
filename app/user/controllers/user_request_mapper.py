from rest_framework.request import Request
from src.common.exception import InvalidOrderDirectionException
from src.common import OrdenDirection
from src.user.services.dto import (SignInDto, SignUpDto, ChangeDataDto, EnableDto, DisableDto, AddRoleDto,
                                   DeleteRoleDto, RenameRoleDto, GiveRoleDto, RemoveRoleDto, FilterUserDto)
from datetime import date

class UserRequestMapper:
    def to_sign_in_dto(self, request: Request) -> SignInDto:
        return SignInDto(
            account = request.data.get('account'),
            password = request.data.get('password')
            )
    
    def to_sign_up_dto(self, request: Request) -> SignUpDto:
        return SignUpDto(
            account = request.data.get('account'),
            name = request.data.get('name'),
            password = request.data.get('password'),
            birthdate = date.fromisoformat(request.data.get('birthdate')),
            roles = request.data.get('roles')
            )
    
    def to_change_data_dto(self, request: Request) -> ChangeDataDto:
        return ChangeDataDto(
            id = request.data.get('id'),
            account = request.data.get('account'),
            name = request.data.get('name'),
            password = request.data.get('password')
        )
    
    def to_enable_dto(self, request: Request) -> EnableDto:
        return EnableDto(id = request.data.get('id'))

    def to_disable_dto(self, request: Request) -> DisableDto:
        return DisableDto(id = request.data.get('id'))
    
    def to_add_role_dto(self, request: Request) -> AddRoleDto:
        return AddRoleDto(role = request.data.get('role'))
    
    def to_delete_role_dto(self, role: str) -> DeleteRoleDto:
        return DeleteRoleDto(role = role)
    
    def to_rename_role_dto(self, request: Request) -> RenameRoleDto:
        return RenameRoleDto(role = request.data.get('role'), new_role = request.data.get('new_role'))
    
    def to_give_role_dto(self, request: Request) -> GiveRoleDto:
        return GiveRoleDto(id = request.data.get('id'), roles = request.data.get('roles'))
    
    def to_remove_role_dto(self, id: str, roles: str) -> RemoveRoleDto:
        role_list = roles.split(',')
        return RemoveRoleDto(id = id, roles = role_list)

    def to_filter_user_dto(self, expresion: str, order_by: int,
                           offset: int, limit: int, direction: str) -> FilterUserDto:
        if not OrdenDirection.contain_name(direction):
            raise InvalidOrderDirectionException.invalid_direction(direction)
        return FilterUserDto(
            expresion = expresion,
            order_by = order_by,
            offset = offset,
            limit = limit,
            direction = OrdenDirection(direction)
        )