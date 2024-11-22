from ...data_providers import ClientUserRepository
from ...domain import ClientUser
from ..dto import ChangeDataDto, ClientUserDto
from ..user_is_registered import UserIsRegistered
from .IChange_account_data import IChangeAccountData
from typing import override

class ChangeAccountData(IChangeAccountData):
    def __init__(self, user_repository: ClientUserRepository) -> None:
        self.__user_repository = user_repository
        
    @override
    def changeData(self, dto: ChangeDataDto) -> ClientUserDto:
        user = UserIsRegistered.is_registered_by_id(self.__user_repository, dto.get_id())
        user = self.__change(user, dto)
        return ClientUserDto.generate_dto(user)
        
    def __change(self, user: ClientUser, dto: ChangeDataDto) -> ClientUser:
        user.change_account(dto.get_account())
        user.change_name(dto.get_name())
        user.change_password(dto.get_password())
        return self.__user_repository.save(user)