from ...data_providers import ClientUserRepository
from ...domain import ClientUser
from ..dto import EnableDto, ClientUserDto
from ..user_is_registered import UserIsRegistered
from .IDisable_client_user_account import IDisableClientUserAccount
from typing import override

class DisableClientUserAccount(IDisableClientUserAccount):
    def __init__(self, user_repository: ClientUserRepository) -> None:
        self.__user_repository = user_repository
        
    @override
    def enable(self, dto: EnableDto) -> ClientUserDto:
        user = UserIsRegistered.is_registered_by_id(self.__user_repository, dto.get_id())
        user = self.__disable_account(user)
        return ClientUserDto.generate_dto(user)
    
    def __disable_account(self, user: ClientUser) -> ClientUser:
        if user.is_enable():
            user.disable()
            return self.__userRepository.save(user)
        return user
        