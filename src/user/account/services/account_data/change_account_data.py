from ...data_providers import SaveUser
from ...domain import UserAccount
from ..dto import ChangeDataDto, UserAccountDto
from ..user_is_registered import UserIsRegistered
from ..user_account_mapper import UserAccountMapper
from .IChange_account_data import IChangeAccountData

class ChangeAccountData(IChangeAccountData):
    def __init__(self, save_user: SaveUser, user_is_registered: UserIsRegistered, 
                 mapper: UserAccountMapper) -> None:
        self.__user_is_registered = user_is_registered
        self.__save_user = save_user
        self.__mapper = mapper
        
    def change_data(self, dto: ChangeDataDto) -> UserAccountDto:
        user = self.__verify(dto)
        user = self.__change(user, dto)
        return self.__mapper.to_dto(user)
        
    def __change(self, user: UserAccount, dto: ChangeDataDto) -> UserAccountDto:
        user.change_account(dto.get_account())
        user.change_name(dto.get_name())
        user.change_password(dto.get_password())
        return self.__save_user.save(user)
    
    def __verify(self, dto: ChangeDataDto) -> UserAccount:
        user = self.__user_is_registered.is_registered_by_id(dto.get_id())
        if dto.get_account() != None and not user.is_my_account(dto.get_account()):
            self.__user_is_registered.verify_is_already_registered(dto.get_account())
        return user