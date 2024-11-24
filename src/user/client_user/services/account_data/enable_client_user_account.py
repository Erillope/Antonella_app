from ...data_providers import ClientUserRepository
from ...domain import ClientUser
from ..dto import EnableDto, ClientUserDto
from ..user_is_registered import UserIsRegistered
from .IEnable_client_user_account import IEnableClientUserAccount
from typing import override
from singleton_decorator import singleton

@singleton
class EnableClientUserAccount(IEnableClientUserAccount):
    def __init__(self, user_repository: ClientUserRepository) -> None:
        self.__user_repository = user_repository
        
    @override
    def enable(self, dto: EnableDto) -> ClientUserDto:
        user = UserIsRegistered.is_registered_by_id(self.__user_repository, dto.get_id())
        user = self.__enable_account(user)
        return ClientUserDto.generate_dto(user)
    
    def __enable_account(self, user: ClientUser) -> ClientUser:
        if not user.is_enable():
            user.enable()
            return self.__user_repository.save(user)
        return user