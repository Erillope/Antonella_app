from ...data_providers import ClientUserRepository
from ...domain import ClientUser
from ..dto import ChangeDataDto, ClientUserDto
from ..user_is_registered import UserIsRegistered
from .IChange_account_data import IChangeAccountData
from singleton_decorator import singleton

@singleton
class ChangeAccountData(IChangeAccountData):
    def __init__(self, user_repository: ClientUserRepository) -> None:
        self.__user_repository = user_repository
        
    def change_data(self, dto: ChangeDataDto) -> ClientUserDto:
        user = self.__verify(dto)
        user = self.__change(user, dto)
        return ClientUserDto.generate_dto(user)
        
    def __change(self, user: ClientUser, dto: ChangeDataDto) -> ClientUser:
        user.change_account(dto.get_account())
        user.change_name(dto.get_name())
        user.change_password(dto.get_password())
        return self.__user_repository.save(user)
    
    def __verify(self, dto: ChangeDataDto) -> ClientUser:
        user = UserIsRegistered.is_registered_by_id(self.__user_repository, dto.get_id())
        if dto.get_account() != None and user.get_account() != dto.get_account():
            UserIsRegistered.verify_is_already_registered(self.__user_repository, dto.get_account())
        return user